# 驱动安装过程中出现dkms编译失败报错

## 内核版本


## 问题现象
在Atlas系列多种硬件设备（如Atlas 200I A2加速模块、Atlas 300I Pro推理卡、Atlas 800训练服务器等）的驱动安装过程中，出现DKMS编译失败报错，具体错误信息为：'[ERROR]Dkms install failed, details in : var/log/ascend_seclog/ascend_install.log' 和 '[ERROR]Driver_ko_install failed, details in : /var/log/ascend_seclog/ascend_install.log'。

## 问题根因
由于dkms工具问题导致驱动编译失败后残留了相关目录（davinci_ascend），影响后续驱动安装。

## 解决方案
1. 进入“/var/lib/dkms”目录；2. 删除“davinci_ascend”目录（执行命令：rm -rf davinci_ascend）；3. 重新安装驱动，具体步骤参考对应产品文档《NPU驱动和固件安装指南》中的“安装驱动”章节。

