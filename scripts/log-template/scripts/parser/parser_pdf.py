from . import register

try:
    import pypdf
except ImportError:
    pypdf = None


@register(".pdf")
def parse_pdf(file_path: str) -> list[str]:
    """解析 PDF 文件：全文作为一个案例"""
    if pypdf is None:
        raise ImportError("解析 PDF 需要安装 pypdf: pip install pypdf")

    reader = pypdf.PdfReader(file_path)
    parts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            parts.append(text)
    content = "\n\n".join(parts).strip()
    return [content] if content else []
