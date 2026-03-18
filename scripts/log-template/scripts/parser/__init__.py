"""
解析器模块：根据文件类型解析输入，返回案例内容列表。
每个案例是一个字符串，将作为 prompt 中的 {content} 传入。
"""
import os

# 解析器注册表：扩展名 -> 解析函数
_parsers = {}


def register(ext: str):
    """装饰器：注册扩展名对应的解析器"""
    def decorator(fn):
        _parsers[ext.lower()] = fn
        return fn
    return decorator


def get_parser(file_path: str):
    """根据文件路径获取对应的解析器"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in _parsers:
        raise ValueError(f"不支持的文件格式: {ext}，当前支持: {list(_parsers.keys())}")
    return _parsers[ext]


def parse(file_path: str) -> list[str]:
    """
    解析文件，返回案例内容列表。
    - txt/md/pdf: 返回 [全文内容]，即一个案例
    - xlsx: 返回 [行1内容, 行2内容, ...]，每行一个案例
    """
    parser = get_parser(file_path)
    return parser(file_path)


def get_supported_extensions() -> list[str]:
    """返回所有支持的文件扩展名"""
    return list(_parsers.keys())


# 导入各解析器以完成注册
from .parser_txt import parse_txt
from .parser_md import parse_md
from .parser_xlsx import parse_xlsx
from .parser_pdf import parse_pdf
