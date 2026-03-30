# 安装CANN包时提示驱动版本不兼容

## 内核版本


## 问题现象
安装CANN软件包时，系统提示“check driver compatibility failed”，报错信息包括：'[ERROR] install failed:check driver compatibility failed.You can add --force to force install or upgrade the driver'，随后安装流程终止。

## 问题根因
当前环境中未安装NPU驱动，或已安装的驱动版本与所安装的CANN版本不兼容。

## 解决方案
1. 执行命令 'npu-smi info' 检查驱动是否已安装及当前驱动版本；若无输出则表示驱动未安装。2. 参考官方文档（如 https://www.hiascend.com/document/detail/zh/canncommercial/800/quickstart/quickstart/releasenote_0000.html）确认与当前CANN版本兼容的驱动版本，并重新安装匹配的驱动和固件。

