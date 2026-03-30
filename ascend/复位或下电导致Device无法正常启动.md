# 复位或下电导致Device无法正常启动

## 内核版本


## 问题现象
在Atlas系列设备（包括Atlas 200I SoC A1核心板、Atlas 300I Pro推理卡、Atlas 300V Pro视频解析卡、Atlas 300I Duo推理卡、Atlas 300V视频解析卡、Atlas 300T训练卡、Atlas 800训练服务器、Atlas 900计算节点等）的软件包安装或升级过程中，若对Device或Host执行了复位或下电操作，会导致固件损坏或升级失败，进而造成Device无法正常启动。

## 问题根因
在软件包安装或升级过程中，对Device或Host进行复位或下电操作，中断了固件写入或升级流程，导致固件损坏或状态不一致，从而引发Device无法正常启动。

## 解决方案
针对Device复位或下电导致的问题：首先对Device连续执行3次复位（使用reboot命令，每次间隔10秒以上）；若仍无法启动，则进行下电重启。针对Host复位或下电导致的问题：若Device能正常启动，则重新升级软件包；若Device无法启动，则采用上述Device问题的解决措施。

