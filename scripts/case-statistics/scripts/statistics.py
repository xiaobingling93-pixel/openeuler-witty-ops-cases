"""
统计报表生成模块
生成各类统计报表：内核版本分布、故障类型分布、硬件平台分布等
"""

import json
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import asdict

from parser import CaseMetadata, extract_keywords, extract_hardware_info


class CaseStatistics:
    """案例统计分析器"""

    def __init__(self, cases: List[CaseMetadata]):
        self.cases = cases
        self.stats = {}

    def generate_all_stats(self) -> Dict[str, Any]:
        """生成所有统计信息"""
        self.stats = {
            'overview': self._generate_overview(),
            'kernel_versions': self._analyze_kernel_versions(),
            'categories': self._analyze_categories(),
            'hardware_platforms': self._analyze_hardware_platforms(),
            'fault_types': self._analyze_fault_types(),
            'keywords': self._analyze_keywords(),
            'field_completeness': self._analyze_field_completeness(),
        }
        return self.stats

    def _generate_overview(self) -> Dict[str, Any]:
        """生成概览统计"""
        return {
            'total_cases': len(self.cases),
            'generated_at': datetime.now().isoformat(),
            'categories_count': len(set(c.category for c in self.cases)),
            'kernel_versions_count': len(set(c.kernel_version for c in self.cases if c.kernel_version)),
        }

    def _analyze_kernel_versions(self) -> Dict[str, Any]:
        """分析内核版本分布"""
        versions = [c.kernel_version for c in self.cases if c.kernel_version]
        version_counter = Counter(versions)

        # 按版本号分组
        version_groups = defaultdict(list)
        for version in versions:
            # 提取主要版本号（如 22.03, 24.03）
            if '22.03' in version:
                version_groups['openEuler 22.03'].append(version)
            elif '24.03' in version:
                version_groups['openEuler 24.03'].append(version)
            elif '4.19' in version:
                version_groups['Kernel 4.19'].append(version)
            elif '5.10' in version:
                version_groups['Kernel 5.10'].append(version)
            elif '6.6' in version:
                version_groups['Kernel 6.6'].append(version)
            else:
                version_groups['其他'].append(version)

        return {
            'total_with_version': len(versions),
            'total_unknown': len(self.cases) - len(versions),
            'top_versions': version_counter.most_common(20),
            'version_groups': {k: len(v) for k, v in version_groups.items()},
        }

    def _analyze_categories(self) -> Dict[str, Any]:
        """分析案例类别分布"""
        categories = [c.category for c in self.cases]
        category_counter = Counter(categories)

        return {
            'distribution': dict(category_counter.most_common()),
            'total_categories': len(category_counter),
        }

    def _analyze_hardware_platforms(self) -> Dict[str, Any]:
        """分析硬件平台分布"""
        all_hardware = {
            'cpu_models': [],
            'network_cards': [],
            'storage_devices': [],
            'server_models': []
        }

        for case in self.cases:
            # 从标题和现象中提取硬件信息
            text = f"{case.title} {case.phenomenon} {case.root_cause}"
            hw_info = extract_hardware_info(text)

            for key in all_hardware:
                all_hardware[key].extend(hw_info[key])

        return {
            'cpu_models': Counter(all_hardware['cpu_models']).most_common(20),
            'network_cards': Counter(all_hardware['network_cards']).most_common(20),
            'storage_devices': Counter(all_hardware['storage_devices']).most_common(20),
            'server_models': Counter(all_hardware['server_models']).most_common(20),
        }

    def _analyze_fault_types(self) -> Dict[str, Any]:
        """分析故障类型分布"""
        fault_types = Counter()

        # 故障类型关键词映射
        fault_keywords = {
            '内核崩溃': ['panic', 'oops', '崩溃', '挂死', '卡死', '死机', '重启'],
            'OOM内存溢出': ['oom', '内存', 'out of memory', '内存溢出'],
            '网络故障': ['网络', '网卡', '网口', 'tcp', 'ip', '连接', 'ssh'],
            '存储故障': ['磁盘', '硬盘', 'nvme', 'raid', 'xfs', '文件系统', '存储'],
            '驱动问题': ['驱动', 'driver', 'module', '模块'],
            'CPU问题': ['cpu', '硬锁', '软锁', 'lockup', '过热', '过温'],
            '启动问题': ['启动', 'boot', 'grub', 'pxe', '安装'],
            '性能问题': ['性能', '劣化', '缓慢', '卡顿', '延迟'],
            '硬件错误': ['硬件', 'hardware', 'pcie', 'i2c', 'sas'],
            '服务异常': ['服务', 'service', 'daemon', 'systemd'],
        }

        for case in self.cases:
            text = f"{case.title} {case.phenomenon} {case.root_cause}".lower()

            for fault_type, keywords in fault_keywords.items():
                for keyword in keywords:
                    if keyword in text:
                        fault_types[fault_type] += 1
                        break

        return {
            'distribution': dict(fault_types.most_common()),
            'total_classified': sum(fault_types.values()),
        }

    def _analyze_keywords(self) -> Dict[str, Any]:
        """分析关键词频率"""
        all_keywords = []

        for case in self.cases:
            text = f"{case.title} {case.phenomenon} {case.root_cause} {case.solution}"
            keywords = extract_keywords(text)
            all_keywords.extend(keywords)

        keyword_counter = Counter(all_keywords)

        return {
            'top_keywords': keyword_counter.most_common(50),
            'total_unique_keywords': len(keyword_counter),
        }

    def _analyze_field_completeness(self) -> Dict[str, Any]:
        """分析字段完整度"""
        total = len(self.cases)

        fields = {
            'title': sum(1 for c in self.cases if c.title),
            'kernel_version': sum(1 for c in self.cases if c.kernel_version),
            'phenomenon': sum(1 for c in self.cases if c.phenomenon),
            'root_cause': sum(1 for c in self.cases if c.root_cause),
            'solution': sum(1 for c in self.cases if c.solution),
        }

        return {
            'total_cases': total,
            'field_counts': fields,
            'field_percentages': {k: f"{v/total*100:.1f}%" for k, v in fields.items()},
        }


class ReportGenerator:
    """报表生成器"""

    def __init__(self, stats: Dict[str, Any], output_dir: str):
        self.stats = stats
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_json_report(self, filename: str = 'statistics_report.json') -> str:
        """生成 JSON 格式报表"""
        output_path = self.output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2)

        return str(output_path)

    def generate_csv_reports(self) -> List[str]:
        """生成多个 CSV 格式报表"""
        generated_files = []

        # 1. 概览报表
        overview_data = [
            ['指标', '值'],
            ['案例总数', self.stats['overview']['total_cases']],
            ['类别数量', self.stats['overview']['categories_count']],
            ['内核版本数量', self.stats['overview']['kernel_versions_count']],
            ['生成时间', self.stats['overview']['generated_at']],
        ]
        overview_path = self._write_csv('overview.csv', overview_data)
        generated_files.append(overview_path)

        # 2. 内核版本分布
        kernel_data = [['内核版本', '案例数量']]
        for version, count in self.stats['kernel_versions']['top_versions']:
            kernel_data.append([version, count])
        kernel_path = self._write_csv('kernel_versions.csv', kernel_data)
        generated_files.append(kernel_path)

        # 3. 类别分布
        category_data = [['类别', '案例数量']]
        for category, count in self.stats['categories']['distribution'].items():
            category_data.append([category, count])
        category_path = self._write_csv('categories.csv', category_data)
        generated_files.append(category_path)

        # 4. 故障类型分布
        fault_data = [['故障类型', '案例数量']]
        for fault_type, count in self.stats['fault_types']['distribution'].items():
            fault_data.append([fault_type, count])
        fault_path = self._write_csv('fault_types.csv', fault_data)
        generated_files.append(fault_path)

        # 5. 硬件平台分布
        hw_data = [['硬件类型', '型号', '案例数量']]
        for hw_type, items in self.stats['hardware_platforms'].items():
            for item, count in items:
                hw_data.append([hw_type, item, count])
        hw_path = self._write_csv('hardware_platforms.csv', hw_data)
        generated_files.append(hw_path)

        # 6. 字段完整度
        completeness_data = [['字段', '填写数量', '完整度']]
        fields = self.stats['field_completeness']['field_counts']
        percentages = self.stats['field_completeness']['field_percentages']
        for field, count in fields.items():
            completeness_data.append([field, count, percentages[field]])
        completeness_path = self._write_csv('field_completeness.csv', completeness_data)
        generated_files.append(completeness_path)

        # 7. 热门关键词
        keyword_data = [['关键词', '出现次数']]
        for keyword, count in self.stats['keywords']['top_keywords']:
            keyword_data.append([keyword, count])
        keyword_path = self._write_csv('top_keywords.csv', keyword_data)
        generated_files.append(keyword_path)

        return generated_files

    def _write_csv(self, filename: str, data: List[List[Any]]) -> str:
        """写入 CSV 文件"""
        output_path = self.output_dir / filename

        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(data)

        return str(output_path)

    def generate_markdown_report(self, filename: str = 'statistics_report.md') -> str:
        """生成 Markdown 格式报表"""
        output_path = self.output_dir / filename

        lines = [
            '# 故障案例统计报表',
            '',
            f'生成时间: {self.stats["overview"]["generated_at"]}',
            '',
            '## 概览',
            '',
            f'- **案例总数**: {self.stats["overview"]["total_cases"]}',
            f'- **类别数量**: {self.stats["overview"]["categories_count"]}',
            f'- **内核版本数量**: {self.stats["overview"]["kernel_versions_count"]}',
            '',
            '## 内核版本分布',
            '',
            '| 内核版本 | 案例数量 |',
            '|----------|----------|',
        ]

        for version, count in self.stats['kernel_versions']['top_versions'][:15]:
            lines.append(f'| {version} | {count} |')

        lines.extend([
            '',
            '## 案例类别分布',
            '',
            '| 类别 | 案例数量 |',
            '|------|----------|',
        ])

        for category, count in self.stats['categories']['distribution'].items():
            lines.append(f'| {category} | {count} |')

        lines.extend([
            '',
            '## 故障类型分布',
            '',
            '| 故障类型 | 案例数量 |',
            '|----------|----------|',
        ])

        for fault_type, count in self.stats['fault_types']['distribution'].items():
            lines.append(f'| {fault_type} | {count} |')

        lines.extend([
            '',
            '## 字段完整度',
            '',
            '| 字段 | 填写数量 | 完整度 |',
            '|------|----------|--------|',
        ])

        fields = self.stats['field_completeness']['field_counts']
        percentages = self.stats['field_completeness']['field_percentages']
        for field, count in fields.items():
            lines.append(f'| {field} | {count} | {percentages[field]} |')

        lines.extend([
            '',
            '## 热门关键词 (Top 20)',
            '',
            '| 关键词 | 出现次数 |',
            '|--------|----------|',
        ])

        for keyword, count in self.stats['keywords']['top_keywords'][:20]:
            lines.append(f'| {keyword} | {count} |')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        return str(output_path)
