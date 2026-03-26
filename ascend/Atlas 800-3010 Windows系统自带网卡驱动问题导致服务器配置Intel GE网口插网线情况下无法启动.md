# Atlas 800-3010 Windows系统自带网卡驱动问题导致服务器配置Intel GE网口插网线情况下无法启动

## 内核版本


## 问题现象
在BIOS默认配置下，服务器配置Intel GE网卡（如I350、82580、82576等）并连接网线时安装Windows Server 2012 R2或Windows Server 2016系统，安装完成后出现蓝屏。在8P以上服务器上问题必现。Windows 2012 R2表现为DPC_WATCHDOG_VIOLATION蓝屏，Windows 2016则直接蓝屏无法启动。

## 问题根因
Windows系统自带的Intel GE网卡驱动存在兼容性问题：1）当BIOS中启用System Errors选项时，驱动会触发不可纠正的硬件错误（WHEA UNCORRECTABLE ERROR），导致系统蓝屏；2）在Windows Server 2012 R2中，连接网线状态下安装后重启会因驱动问题引发DPC_WATCHDOG_VIOLATION蓝屏。

## 解决方案
1. 安装Windows系统前，在BIOS中关闭System Errors选项（路径：A800-3010为Advanced -> System Event log -> System Errors；V3服务器为IntelRCSetup -> Runtime Error Logging -> System Errors），并拔掉Intel GE网卡的网线；2. 系统安装完成后，使用厂商提供的idriver工具更新Intel GE网卡驱动；3. 驱动更新后，可重新在BIOS中开启System Errors选项。

