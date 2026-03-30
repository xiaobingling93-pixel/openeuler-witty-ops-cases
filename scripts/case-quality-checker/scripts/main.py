"""
案例质量检查器
检查案例文件是否符合标准模板格式，验证必填字段完整性
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class CaseQualityChecker:
    """案例质量检查器"""

    def __init__(self):
        self.required_fields = {
            '#标题': {'required': True, 'aliases': ['# 标题', '标题']},
            '#内核版本': {'required': True, 'aliases': ['# 内核版本', '内核版本']},
            '#问题现象': {'required': True, 'aliases': ['# 问题现象', '问题现象']},
            '#问题根因': {'required': True, 'aliases': ['# 问题根因', '问题根因', '#根因', '# 根因']},
            '#解决方案': {'required': True, 'aliases': ['# 解决方案', '解决方案', '#解决措施', '# 解决措施']},
        }

    def check_file(self, file_path: str) -> Dict:
        """检查单个案例文件"""
        path = Path(file_path)
        result = {
            'file_path': str(path),
            'file_name': path.name,
            'is_valid': True,
            'missing_fields': [],
            'empty_fields': [],
            'format_errors': [],
            'warnings': []
        }

        if not path.exists():
            result['is_valid'] = False
            result['format_errors'].append('文件不存在')
            return result

        if path.suffix.lower() not in ['.txt', '.md']:
            result['warnings'].append(f'不支持的文件类型: {path.suffix}')
            return result

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if not content.strip():
                result['is_valid'] = False
                result['format_errors'].append('文件内容为空')
                return result

            lines = content.split('\n')
            found_fields = set()

            for i, line in enumerate(lines):
                line_stripped = line.strip()

                for field, config in self.required_fields.items():
                    all_names = [field] + config['aliases']
                    for name in all_names:
                        if line_stripped.startswith(name):
                            found_fields.add(field)
                            break

            for field, config in self.required_fields.items():
                if config['required'] and field not in found_fields:
                    result['missing_fields'].append(field)
                    result['is_valid'] = False

            for field in found_fields:
                field_content = self._extract_field_content(content, field)
                if not field_content or len(field_content.strip()) < 5:
                    result['empty_fields'].append(field)
                    result['warnings'].append(f'字段内容过短: {field}')

            if result['missing_fields']:
                result['format_errors'].append(f'缺少必填字段: {", ".join(result["missing_fields"])}')

        except Exception as e:
            result['is_valid'] = False
            result['format_errors'].append(f'读取文件失败: {str(e)}')

        return result

    def _extract_field_content(self, content: str, field: str) -> str:
        """提取字段内容"""
        lines = content.split('\n')
        config = self.required_fields.get(field, {})
        all_names = [field] + config.get('aliases', [])

        for i, line in enumerate(lines):
            line_stripped = line.strip()
            for name in all_names:
                if line_stripped.startswith(name):
                    content_start = line_stripped[len(name):].strip()
                    if content_start:
                        return content_start
                    if i + 1 < len(lines):
                        result = []
                        for j in range(i + 1, len(lines)):
                            next_line = lines[j].strip()
                            if next_line.startswith('#') or next_line == '':
                                if result:
                                    break
                                continue
                            result.append(next_line)
                        return '\n'.join(result).strip()

        return ""

    def check_directory(self, dir_path: str, recursive: bool = True) -> List[Dict]:
        """检查目录下的所有案例文件"""
        path = Path(dir_path)
        results = []

        if not path.exists() or not path.is_dir():
            print(f'错误: 目录不存在: {dir_path}')
            return results

        pattern = '**/*' if recursive else '*'

        for file_path in path.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in ['.txt', '.md']:
                result = self.check_file(str(file_path))
                results.append(result)

        return results

    def generate_report(self, results: List[Dict]) -> Dict:
        """生成质量报告"""
        total = len(results)
        valid = sum(1 for r in results if r['is_valid'])
        invalid = total - valid

        missing_field_stats = {}
        for result in results:
            for field in result['missing_fields']:
                missing_field_stats[field] = missing_field_stats.get(field, 0) + 1

        empty_field_stats = {}
        for result in results:
            for field in result['empty_fields']:
                empty_field_stats[field] = empty_field_stats.get(field, 0) + 1

        return {
            'total_cases': total,
            'valid_cases': valid,
            'invalid_cases': invalid,
            'valid_rate': f'{valid/total*100:.1f}%' if total > 0 else '0%',
            'missing_field_stats': missing_field_stats,
            'empty_field_stats': empty_field_stats,
            'details': results
        }


def print_console_report(report: Dict, verbose: bool = False):
    """打印控制台报告"""
    print('=' * 70)
    print('案例质量检查报告')
    print('=' * 70)
    print(f'总案例数: {report["total_cases"]}')
    print(f'有效案例: {report["valid_cases"]} ({report["valid_rate"]})')
    print(f'无效案例: {report["invalid_cases"]}')
    print()

    if report['missing_field_stats']:
        print('缺失字段统计:')
        for field, count in sorted(report['missing_field_stats'].items(), key=lambda x: x[1], reverse=True):
            print(f'  {field}: {count} 个案例')
        print()

    if report['empty_field_stats']:
        print('内容过短字段:')
        for field, count in sorted(report['empty_field_stats'].items(), key=lambda x: x[1], reverse=True):
            print(f'  {field}: {count} 个案例')
        print()

    if verbose and report['invalid_cases'] > 0:
        print('无效案例详情:')
        for result in report['details']:
            if not result['is_valid']:
                print(f'\n  文件: {result["file_name"]}')
                if result['missing_fields']:
                    print(f'    缺失字段: {", ".join(result["missing_fields"])}')
                if result['empty_fields']:
                    print(f'    内容过短: {", ".join(result["empty_fields"])}')
                if result['format_errors']:
                    print(f'    格式错误: {"; ".join(result["format_errors"])}')
        print()

    print('=' * 70)


def save_report_to_file(report: Dict, output_path: str):
    """保存报告到文件"""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        '# 案例质量检查报告',
        '',
        f'总案例数: {report["total_cases"]}',
        f'有效案例: {report["valid_cases"]} ({report["valid_rate"]})',
        f'无效案例: {report["invalid_cases"]}',
        '',
    ]

    if report['missing_field_stats']:
        lines.append('## 缺失字段统计')
        lines.append('')
        lines.append('| 字段 | 缺失数量 |')
        lines.append('|------|----------|')
        for field, count in sorted(report['missing_field_stats'].items(), key=lambda x: x[1], reverse=True):
            lines.append(f'| {field} | {count} |')
        lines.append('')

    if report['empty_field_stats']:
        lines.append('## 内容过短字段')
        lines.append('')
        lines.append('| 字段 | 案例数量 |')
        lines.append('|------|----------|')
        for field, count in sorted(report['empty_field_stats'].items(), key=lambda x: x[1], reverse=True):
            lines.append(f'| {field} | {count} |')
        lines.append('')

    if report['invalid_cases'] > 0:
        lines.append('## 无效案例详情')
        lines.append('')
        for result in report['details']:
            if not result['is_valid']:
                lines.append(f'### {result["file_name"]}')
                lines.append(f'**路径**: `{result["file_path"]}`')
                if result['missing_fields']:
                    lines.append(f'**缺失字段**: {", ".join(result["missing_fields"])}')
                if result['empty_fields']:
                    lines.append(f'**内容过短**: {", ".join(result["empty_fields"])}')
                if result['format_errors']:
                    lines.append(f'**格式错误**: {"; ".join(result["format_errors"])}')
                if result['warnings']:
                    lines.append(f'**警告**: {"; ".join(result["warnings"])}')
                lines.append('')

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='案例质量检查器 - 检查案例文件是否符合标准模板格式',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python scripts/main.py ../../community_maintenance
  python scripts/main.py ../../community_maintenance -o report.md -v
  python scripts/main.py ../../community_maintenance --no-recursive
        '''
    )

    parser.add_argument(
        'input_dir',
        help='案例文件所在目录路径'
    )

    parser.add_argument(
        '-o', '--output',
        help='输出报告文件路径（可选，支持 .md 格式）'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细错误信息'
    )

    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        default=True,
        help='递归扫描子目录（默认开启）'
    )

    parser.add_argument(
        '--no-recursive',
        action='store_true',
        help='不递归扫描子目录'
    )

    args = parser.parse_args()

    input_path = Path(args.input_dir).resolve()
    if not input_path.exists():
        print(f'错误: 输入目录不存在: {input_path}')
        sys.exit(1)

    recursive = not args.no_recursive

    print('正在检查案例质量...')
    checker = CaseQualityChecker()
    results = checker.check_directory(str(input_path), recursive=recursive)

    if not results:
        print('警告: 未找到任何案例文件')
        sys.exit(0)

    report = checker.generate_report(results)

    print_console_report(report, verbose=args.verbose)

    if args.output:
        save_report_to_file(report, args.output)
        print(f'报告已保存到: {args.output}')

    if report['invalid_cases'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
