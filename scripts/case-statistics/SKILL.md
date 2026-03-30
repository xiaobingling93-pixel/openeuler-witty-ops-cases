---
name: case-statistics
description: 故障案例统计报表生成器，分析案例库并生成多维度的统计报表（内核版本分布、故障类型、硬件平台、字段完整度等），支持 JSON、CSV、Markdown 格式输出。
---

# 案例统计报表生成器

## 功能概述

本工具用于分析故障案例库，生成多维度的统计报表，帮助团队了解故障分布趋势和知识库质量。

### 统计维度

1. **概览统计** - 案例总数、类别数、内核版本数
2. **内核版本分布** - 各版本案例数量、版本分组统计
3. **案例类别分布** - 按文件夹/类别统计
4. **硬件平台分布** - CPU、网卡、存储、服务器型号
5. **故障类型分布** - 内核崩溃、OOM、网络故障、存储故障等
6. **关键词分析** - 高频关键词提取
7. **字段完整度** - 标题、内核版本、现象、根因、解决方案的填写率

## 触发场景

- 需要了解案例库整体情况
- 定期生成故障分析报告
- 评估知识库质量和完整度
- 发现故障趋势和热点问题

## 执行方式

在 `case-statistics` 目录下运行：

```bash
# 基本用法 - 分析指定目录，生成所有格式报表
python scripts/main.py <案例目录路径>

# 示例：分析 community_maintenance 目录
python scripts/main.py ../../community_maintenance

# 指定输出目录
python scripts/main.py ../../community_maintenance -o ./reports

# 只生成特定格式
python scripts/main.py ../../community_maintenance -f json    # 只生成 JSON
python scripts/main.py ../../community_maintenance -f csv     # 只生成 CSV
python scripts/main.py ../../community_maintenance -f md      # 只生成 Markdown

# 不递归扫描子目录
python scripts/main.py ../../community_maintenance --no-recursive
```

## 输出文件

运行后会在输出目录（默认 `output/`）生成以下文件：

### 当选择 `all` 或 `json` 格式时：
- `statistics_report.json` - 完整的统计信息（JSON 格式）

### 当选择 `all` 或 `csv` 格式时：
- `overview.csv` - 概览统计
- `kernel_versions.csv` - 内核版本分布
- `categories.csv` - 类别分布
- `fault_types.csv` - 故障类型分布
- `hardware_platforms.csv` - 硬件平台分布
- `field_completeness.csv` - 字段完整度
- `top_keywords.csv` - 热门关键词

### 当选择 `all` 或 `md` 格式时：
- `statistics_report.md` - Markdown 格式汇总报表

## 依赖

本工具主要使用 Python 标准库，无需额外安装依赖：

```bash
# 可选：安装依赖（如果需要使用可选功能）
pip install -r scripts/requirements.txt
```

## 案例文件格式要求

工具支持解析标准格式的案例文件（.txt 或 .md），期望包含以下字段：

```
#标题
案例标题

#内核版本
内核版本号

#问题现象
问题描述...

#问题根因
根因分析...

#解决方案
解决措施...
```

## 示例输出

### 控制台输出示例

```
============================================================
故障案例统计报表生成器
============================================================
输入目录: D:\Git\witty-ops-cases-master\community_maintenance
输出目录: D:\Git\witty-ops-cases-master\scripts\case-statistics\output
递归扫描: True
输出格式: all
============================================================

步骤 1/3: 正在解析案例文件...
  ✓ 成功解析 245 个案例

步骤 2/3: 正在生成统计信息...
  ✓ 统计信息生成完成
    - 案例总数: 245
    - 内核版本数: 18
    - 类别数: 1

步骤 3/3: 正在生成报表...
  ✓ JSON 报表: D:\...\output\statistics_report.json
  ✓ CSV 报表: 7 个文件
    - overview.csv
    - kernel_versions.csv
    - categories.csv
    - fault_types.csv
    - hardware_platforms.csv
    - field_completeness.csv
    - top_keywords.csv
  ✓ Markdown 报表: D:\...\output\statistics_report.md

============================================================
报表生成完成!
============================================================

📊 统计摘要:
  案例总数: 245
  有版本信息: 189 (77.1%)
  版本未知: 56

  故障类型分布:
    - 内核崩溃: 45
    - 网络故障: 38
    - 驱动问题: 32
    - OOM内存溢出: 28
    - 存储故障: 25

  字段完整度:
    - title: 100.0%
    - kernel_version: 77.1%
    - phenomenon: 95.5%
    - root_cause: 92.2%
    - solution: 88.6%
```

## 故障类型识别规则

工具通过关键词匹配自动识别故障类型：

| 故障类型 | 识别关键词 |
|----------|------------|
| 内核崩溃 | panic, oops, 崩溃, 挂死, 卡死, 死机, 重启 |
| OOM内存溢出 | oom, 内存, out of memory, 内存溢出 |
| 网络故障 | 网络, 网卡, 网口, tcp, ip, 连接, ssh |
| 存储故障 | 磁盘, 硬盘, nvme, raid, xfs, 文件系统, 存储 |
| 驱动问题 | 驱动, driver, module, 模块 |
| CPU问题 | cpu, 硬锁, 软锁, lockup, 过热, 过温 |
| 启动问题 | 启动, boot, grub, pxe, 安装 |
| 性能问题 | 性能, 劣化, 缓慢, 卡顿, 延迟 |
| 硬件错误 | 硬件, hardware, pcie, i2c, sas |
| 服务异常 | 服务, service, daemon, systemd |

## 扩展开发

如需添加新的统计维度或输出格式，可以修改以下文件：

1. `scripts/parser.py` - 案例解析逻辑
2. `scripts/statistics.py` - 统计分析和报表生成
3. `scripts/main.py` - 命令行接口

## 注意事项

1. 工具会跳过无法解析的文件，并在控制台显示警告
2. 内核版本识别基于文本匹配，可能无法识别所有格式
3. 硬件信息从标题和现象文本中提取，可能存在遗漏
4. 建议定期运行统计，跟踪知识库质量变化
