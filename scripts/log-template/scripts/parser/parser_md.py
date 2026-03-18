from . import register


@register(".md")
def parse_md(file_path: str) -> list[str]:
    """解析 md 文件：全文作为一个案例"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return [content] if content.strip() else []
