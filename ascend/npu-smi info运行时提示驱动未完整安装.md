# npu-smi info运行时提示驱动未完整安装

## 内核版本


## 问题现象
在Atlas系列设备（如Atlas 300T训练卡、Atlas 800训练服务器等）上安装驱动后，执行npu-smi info命令时出现警告：'[WARNING]The driver package may not be completely installed, which may cause function abnormal. Please reinstall it.'

## 问题根因
系统文件“/etc/ascend_install.info”中缺少“Driver_Install_Status=complete”字段，表明驱动未被完整安装，导致npu-smi工具检测到异常并发出警告。

## 解决方案
重新安装NPU驱动，具体操作步骤请参考对应产品的《NPU驱动和固件安装指南》中“安装驱动”章节。

