"""
案例统计报表生成器主程序

用法:
  python scripts/main.py <案例目录路径> [选项]

选项:
  -o, --output <目录>    指定输出目录（默认: output）
  -f, --format <格式>    输出格式: json, csv, md, all（默认: all）
  -r, --recursive        递归扫描子目录（默认开启）
  --no-recursive         不递归扫描子目录

示例:
  python scripts/main.py ../../community_maintenance
  python scripts/main.py ../../community_maintenance -o ./reports -f json
  python scripts/main.py ../../community_maintenance --format csv
"""

import argparse
import sys
from pathlib import Path

from parser import CaseParser
from statistics import CaseStatistics, ReportGenerator


def main():
    parser = argparse.ArgumentParser(
        description='故障案例统计报表生成器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python scripts/main.py ../../community_maintenance
  python scripts/main.py ../../community_maintenance -o ./reports -f json
  python scripts/main.py ../../community_maintenance --format csv
        '''
    )

    parser.add_argument(
        'input_dir',
        help='案例文件所在目录路径'
    )

    parser.add_argument(
        '-o', '--output',
        default='output',
        help='输出目录路径（默认: output）'
    )

    parser.add_argument(
        '-f', '--format',
        choices=['json', 'csv', 'md', 'all'],
        default='all',
        help='输出格式（默认: all）'
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

    # 解析输入路径
    input_path = Path(args.input_dir).resolve()
    if not input_path.exists():
        print(f'错误: 输入目录不存在: {input_path}')
        sys.exit(1)

    if not input_path.is_dir():
        print(f'错误: 输入路径不是目录: {input_path}')
        sys.exit(1)

    # 解析输出路径
    output_path = Path(args.output).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    # 是否递归
    recursive = not args.no_recursive

    print('=' * 60)
    print('故障案例统计报表生成器')
    print('=' * 60)
    print(f'输入目录: {input_path}')
    print(f'输出目录: {output_path}')
    print(f'递归扫描: {recursive}')
    print(f'输出格式: {args.format}')
    print('=' * 60)
    print()

    # 第一步：解析案例文件
    print('步骤 1/3: 正在解析案例文件...')
    case_parser = CaseParser()
    cases = case_parser.parse_directory(str(input_path), recursive=recursive)

    if not cases:
        print('警告: 未找到任何案例文件')
        sys.exit(0)

    print(f'  ✓ 成功解析 {len(cases)} 个案例')

    # 显示解析统计
    stats = case_parser.get_stats()
    if stats['parsed_failed'] > 0:
        print(f'  ⚠ 解析失败: {stats["parsed_failed"]} 个文件')
        for error in stats['errors'][:5]:  # 只显示前5个错误
            print(f'    - {error}')

    print()

    # 第二步：生成统计信息
    print('步骤 2/3: 正在生成统计信息...')
    statistics = CaseStatistics(cases)
    all_stats = statistics.generate_all_stats()
    print(f'  ✓ 统计信息生成完成')
    print(f'    - 案例总数: {all_stats["overview"]["total_cases"]}')
    print(f'    - 内核版本数: {all_stats["overview"]["kernel_versions_count"]}')
    print(f'    - 类别数: {all_stats["overview"]["categories_count"]}')
    print()

    # 第三步：生成报表
    print('步骤 3/3: 正在生成报表...')
    report_generator = ReportGenerator(all_stats, str(output_path))

    generated_files = []

    if args.format in ['json', 'all']:
        json_file = report_generator.generate_json_report()
        generated_files.append(json_file)
        print(f'  ✓ JSON 报表: {json_file}')

    if args.format in ['csv', 'all']:
        csv_files = report_generator.generate_csv_reports()
        generated_files.extend(csv_files)
        print(f'  ✓ CSV 报表: {len(csv_files)} 个文件')
        for f in csv_files:
            print(f'    - {Path(f).name}')

    if args.format in ['md', 'all']:
        md_file = report_generator.generate_markdown_report()
        generated_files.append(md_file)
        print(f'  ✓ Markdown 报表: {md_file}')

    print()
    print('=' * 60)
    print('报表生成完成!')
    print(f'输出目录: {output_path}')
    print(f'生成文件数: {len(generated_files)}')
    print('=' * 60)

    # 打印统计摘要
    print()
    print('📊 统计摘要:')
    print(f'  案例总数: {all_stats["overview"]["total_cases"]}')
    print(f'  有版本信息: {all_stats["kernel_versions"]["total_with_version"]} ({all_stats["kernel_versions"]["total_with_version"]/all_stats["overview"]["total_cases"]*100:.1f}%)')
    print(f'  版本未知: {all_stats["kernel_versions"]["total_unknown"]}')
    print()
    print('  故障类型分布:')
    for fault_type, count in list(all_stats['fault_types']['distribution'].items())[:5]:
        print(f'    - {fault_type}: {count}')
    print()
    print('  字段完整度:')
    for field, percentage in all_stats['field_completeness']['field_percentages'].items():
        print(f'    - {field}: {percentage}')


if __name__ == '__main__':
    main()
