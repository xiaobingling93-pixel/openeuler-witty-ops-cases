"""
故障案例模板生成脚本
从 txt/md/xlsx/pdf 文件读取故障文档，调用大模型生成标准化模板，输出到 output/ 目录

用法:
  python scripts/template.py file <文件路径>     # 处理单个文件
  python scripts/template.py folder <文件夹路径> # 批量处理文件夹内所有支持格式的文档
  python scripts/template.py -o <输出目录>       # 指定输出目录（可选）
"""
import argparse
import os
import sys
import json
from pathlib import Path

from openai import OpenAI

from parser import parse, get_supported_extensions

# 脚本所在目录（用于解析相对路径）
SCRIPT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = SCRIPT_DIR / "config.json"
PROMPT_PATH = SCRIPT_DIR / "prompt.txt"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "output"


def load_config():
    """从 config.json 加载大模型配置"""
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_prompt() -> str:
    """从 prompt.txt 加载提示词模板，需包含 {content} 占位符"""
    with open(PROMPT_PATH, 'r', encoding='utf-8') as f:
        return f.read()


# 模型输出此标记时表示跳过该案例（文档不合适）
SKIP_MARKER = "#跳过"


def should_skip(result: str) -> bool:
    """判断模型是否要求跳过该案例（文档内容不合适）"""
    first_line = result.strip().split('\n')[0].strip() if result.strip() else ""
    return first_line == SKIP_MARKER or first_line.startswith(SKIP_MARKER + " ")


def extract_title(result: str) -> str:
    """
    从生成结果中提取标题（#标题 下一行的内容）
    若无法提取或为空，返回「未命名案例」
    """
    lines = result.strip().split('\n')
    for i, line in enumerate(lines):
        if line.strip() == '#标题' and i + 1 < len(lines):
            title = lines[i + 1].strip()
            if title:
                for c in r'\/:*?"<>|':
                    title = title.replace(c, '_')
                return title.strip()
    return "未命名案例"


def ensure_unique_path(output_dir: Path, base_name: str, ext: str = ".txt") -> Path:
    """确保输出路径唯一，若重名则添加 _1, _2..."""
    path = output_dir / f"{base_name}{ext}"
    if not path.exists():
        return path
    n = 1
    while True:
        path = output_dir / f"{base_name}_{n}{ext}"
        if not path.exists():
            return path
        n += 1


def generate_template(client: OpenAI, config: dict, prompt_template: str, content: str) -> str:
    """调用大模型生成模板"""
    prompt = prompt_template.replace("{content}", content)
    messages = [{"role": "user", "content": prompt}]
    try:
        completion = client.chat.completions.create(
            model=config.get("model", "qwen3-max"),
            messages=messages,
            extra_body={"enable_thinking": config.get("enable_thinking", False)},
            timeout=config.get("timeout", 180),
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"# 错误\n无法生成模板: {str(e)}"


def resolve_path(path: str) -> Path:
    """将路径解析为绝对路径"""
    p = Path(path)
    if not p.is_absolute():
        p = Path.cwd() / p
    return p.resolve()


def process_file(
    file_path: Path,
    client: OpenAI,
    config: dict,
    prompt_template: str,
    output_dir: Path,
) -> tuple[int, int]:
    """
    处理单个文件，返回 (成功数, 跳过数)
    """
    try:
        cases = parse(str(file_path))
    except (ValueError, ImportError) as e:
        print(f"  解析失败: {e}")
        return 0, 0

    if not cases:
        print(f"  未解析到任何案例内容，跳过")
        return 0, 0

    saved = 0
    skipped = 0
    for i, content in enumerate(cases):
        idx_str = f"[{i+1}/{len(cases)}]"
        print(f"  {idx_str} 正在调用 AI 生成模板...")
        result = generate_template(client, config, prompt_template, content)

        if should_skip(result):
            reason = result.strip().split('\n')[1].strip() if len(result.strip().split('\n')) > 1 else ""
            print(f"  {idx_str} 已跳过（文档不合适）{f': {reason}' if reason else ''}")
            skipped += 1
            continue

        title = extract_title(result)
        output_path = ensure_unique_path(output_dir, title)
        output_path.write_text(result, encoding='utf-8')
        print(f"  {idx_str} 已保存: {output_path.name}")
        saved += 1

    return saved, skipped


def cmd_file(args):
    """处理单个文件"""
    file_path = resolve_path(args.path)
    if not file_path.exists():
        print(f"错误: 文件不存在 {file_path}")
        sys.exit(1)
    if not file_path.is_file():
        print(f"错误: 路径不是文件，请使用 folder 子命令处理文件夹")
        sys.exit(1)

    output_dir = resolve_path(args.output) if args.output else DEFAULT_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    config = load_config()
    prompt_template = load_prompt()
    if "{content}" not in prompt_template:
        print("错误: prompt.txt 中必须包含 {content} 占位符")
        sys.exit(1)

    client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])

    print(f"正在处理文件: {file_path}")
    saved, skipped = process_file(
        file_path, client, config, prompt_template, output_dir
    )
    print(f"\n完成: 保存 {saved} 个，跳过 {skipped} 个")
    print(f"输出目录: {output_dir}")


def cmd_folder(args):
    """批量处理文件夹内所有支持格式的文档"""
    folder_path = resolve_path(args.path)
    if not folder_path.exists():
        print(f"错误: 文件夹不存在 {folder_path}")
        sys.exit(1)
    if not folder_path.is_dir():
        print(f"错误: 路径不是文件夹")
        sys.exit(1)

    output_dir = resolve_path(args.output) if args.output else DEFAULT_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    exts = get_supported_extensions()
    files = [
        f for f in folder_path.iterdir()
        if f.is_file() and f.suffix.lower() in exts
    ]
    files.sort(key=lambda x: x.name)

    if not files:
        print(f"错误: 文件夹内没有支持格式的文档")
        print(f"支持格式: {', '.join(exts)}")
        sys.exit(1)

    print(f"正在处理文件夹: {folder_path}")
    print(f"找到 {len(files)} 个文件: {[f.name for f in files]}")

    config = load_config()
    prompt_template = load_prompt()
    if "{content}" not in prompt_template:
        print("错误: prompt.txt 中必须包含 {content} 占位符")
        sys.exit(1)

    client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])

    total_saved = 0
    total_skipped = 0

    for file_path in files:
        print(f"\n--- {file_path.name} ---")
        saved, skipped = process_file(
            file_path, client, config, prompt_template, output_dir,
        )
        total_saved += saved
        total_skipped += skipped

    print(f"\n全部完成: 保存 {total_saved} 个，跳过 {total_skipped} 个")
    print(f"输出目录: {output_dir}")


def main():
    exts = get_supported_extensions()
    parser = argparse.ArgumentParser(
        description="故障案例模板生成工具，将故障文档转化为标准化模板",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
示例:
  python scripts/template.py file 故障案例.txt
  python scripts/template.py folder ./文档目录/
  python scripts/template.py folder ./docs -o ./output

支持格式: {', '.join(exts)}
        """,
    )
    parser.add_argument(
        "-o", "--output",
        help="输出目录（默认: scripts/output）",
        metavar="DIR",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # file 子命令
    p_file = subparsers.add_parser("file", help="处理单个文件")
    p_file.add_argument("path", help="文件路径")
    p_file.set_defaults(func=cmd_file)

    # folder 子命令
    p_folder = subparsers.add_parser("folder", help="批量处理文件夹内所有文档")
    p_folder.add_argument("path", help="文件夹路径")
    p_folder.set_defaults(func=cmd_folder)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
