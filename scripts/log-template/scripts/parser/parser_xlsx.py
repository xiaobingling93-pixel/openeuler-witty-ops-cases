from . import register

try:
    import openpyxl
except ImportError:
    openpyxl = None


@register(".xlsx")
def parse_xlsx(file_path: str) -> list[str]:
    """
    解析 xlsx 文件：每一行作为一个独立案例。
    第一行作为表头，后续每行转换为 "列名: 值" 格式的文本。
    """
    if openpyxl is None:
        raise ImportError("解析 xlsx 需要安装 openpyxl: pip install openpyxl")

    wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))

    if not rows:
        return []

    headers = [str(h) if h is not None else f"列{i+1}" for i, h in enumerate(rows[0])]
    cases = []

    for row in rows[1:]:
        parts = []
        for i, cell in enumerate(row):
            header = headers[i] if i < len(headers) else f"列{i+1}"
            value = cell if cell is not None else ""
            if str(value).strip():
                parts.append(f"{header}: {value}")
        if parts:
            cases.append("\n".join(parts))
        else:
            # 空行也保留为占位，避免行号错位（可选：可跳过空行）
            cases.append("")

    wb.close()
    return [c for c in cases if c.strip()]
