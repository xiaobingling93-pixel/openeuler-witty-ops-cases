"""
案例文件解析模块
从案例文件中提取元数据（标题、内核版本、问题现象、根因、解决方案）
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CaseMetadata:
    """案例元数据结构"""
    title: str
    kernel_version: str
    phenomenon: str
    root_cause: str
    solution: str
    file_path: str
    file_name: str
    category: str  # 案例类别（从文件夹名推断）


class CaseParser:
    """案例文件解析器"""

    # 字段标记映射
    FIELD_MARKERS = {
        'title': ['#标题', '# 标题', '标题'],
        'kernel_version': ['#内核版本', '# 内核版本', '内核版本'],
        'phenomenon': ['#问题现象', '# 问题现象', '问题现象'],
        'root_cause': ['#问题根因', '# 问题根因', '问题根因', '#根因', '# 根因'],
        'solution': ['#解决方案', '# 解决方案', '解决方案', '#解决措施', '# 解决措施'],
    }

    def __init__(self):
        self.stats = {
            'total_files': 0,
            'parsed_success': 0,
            'parsed_failed': 0,
            'errors': []
        }

    def parse_file(self, file_path: str) -> Optional[CaseMetadata]:
        """解析单个案例文件"""
        try:
            path = Path(file_path)
            if not path.exists() or not path.is_file():
                return None

            # 只处理 txt 和 md 文件
            if path.suffix.lower() not in ['.txt', '.md']:
                return None

            self.stats['total_files'] += 1

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # 提取各个字段
            title = self._extract_field(content, 'title')
            kernel_version = self._extract_field(content, 'kernel_version')
            phenomenon = self._extract_field(content, 'phenomenon')
            root_cause = self._extract_field(content, 'root_cause')
            solution = self._extract_field(content, 'solution')

            # 如果标题为空，尝试从文件名提取
            if not title:
                title = path.stem

            # 推断案例类别（从父文件夹名）
            category = self._infer_category(path)

            self.stats['parsed_success'] += 1

            return CaseMetadata(
                title=title,
                kernel_version=kernel_version,
                phenomenon=phenomenon,
                root_cause=root_cause,
                solution=solution,
                file_path=str(path.absolute()),
                file_name=path.name,
                category=category
            )

        except Exception as e:
            self.stats['parsed_failed'] += 1
            self.stats['errors'].append(f"{file_path}: {str(e)}")
            return None

    def _extract_field(self, content: str, field_name: str) -> str:
        """从内容中提取指定字段"""
        markers = self.FIELD_MARKERS.get(field_name, [])

        lines = content.split('\n')
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            for marker in markers:
                if line_stripped.startswith(marker):
                    # 获取标记后的内容（可能在同一行或下一行）
                    content_start = line_stripped[len(marker):].strip()
                    if content_start:
                        return content_start

                    # 内容在下一行
                    if i + 1 < len(lines):
                        result = []
                        for j in range(i + 1, len(lines)):
                            next_line = lines[j].strip()
                            # 遇到下一个标记或空行结束
                            if next_line.startswith('#') or next_line == '':
                                if result:
                                    break
                                continue
                            result.append(next_line)
                        return '\n'.join(result).strip()

        return ""

    def _infer_category(self, path: Path) -> str:
        """从文件路径推断案例类别"""
        # 获取父文件夹名
        parent = path.parent.name

        # 映射常见类别
        category_map = {
            'community_maintenance': '社区维护',
            'ai_computing': 'AI计算',
            'general_computing': '通用计算',
            'community': '社区维护',
            'ai': 'AI计算',
            'general': '通用计算',
        }

        return category_map.get(parent.lower(), parent)

    def parse_directory(self, dir_path: str, recursive: bool = True) -> List[CaseMetadata]:
        """解析目录下的所有案例文件"""
        cases = []
        path = Path(dir_path)

        if not path.exists() or not path.is_dir():
            return cases

        pattern = '**/*' if recursive else '*'

        for file_path in path.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in ['.txt', '.md']:
                case = self.parse_file(str(file_path))
                if case:
                    cases.append(case)

        return cases

    def get_stats(self) -> dict:
        """获取解析统计信息"""
        return self.stats.copy()


def extract_keywords(text: str, min_length: int = 2) -> List[str]:
    """从文本中提取关键词"""
    if not text:
        return []

    # 简单的关键词提取：中文词汇和英文单词
    # 中文：连续的中文字符
    chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,}', text)

    # 英文：字母数字组合（技术术语）
    english_words = re.findall(r'[a-zA-Z][a-zA-Z0-9_]{1,}', text)

    # 合并并去重
    keywords = list(set(chinese_words + english_words))

    # 过滤太短的词
    keywords = [k for k in keywords if len(k) >= min_length]

    return keywords


def extract_hardware_info(text: str) -> dict:
    """从文本中提取硬件相关信息"""
    info = {
        'cpu_models': [],
        'network_cards': [],
        'storage_devices': [],
        'server_models': []
    }

    if not text:
        return info

    # CPU 型号模式
    cpu_patterns = [
        r'920[BSCG]?',
        r'鲲鹏[0-9]+',
        r'Intel[\s\w]+',
        r'AMD[\s\w]+',
    ]

    # 网卡模式
    nic_patterns = [
        r'hns3',
        r'hinic3',
        r'hisdk3',
        r'hiudk3',
        r'Mellanox',
        r'X710',
    ]

    # 存储设备模式
    storage_patterns = [
        r'NVMe',
        r'RAID',
        r'SAS',
        r'SATA',
        r'XFS',
    ]

    # 服务器型号模式
    server_patterns = [
        r'[0-9]+P[0-9]+U',
        r'A3[\s\w]*',
        r'HPC[\s\w]*',
    ]

    for pattern in cpu_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info['cpu_models'].extend(matches)

    for pattern in nic_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info['network_cards'].extend(matches)

    for pattern in storage_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info['storage_devices'].extend(matches)

    for pattern in server_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        info['server_models'].extend(matches)

    # 去重
    for key in info:
        info[key] = list(set(info[key]))

    return info
