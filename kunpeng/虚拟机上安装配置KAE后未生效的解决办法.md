# 虚拟机上安装配置KAE后未生效的解决办法

## 内核版本


## 问题现象
在HostOS为openEuler 22.03 LTS SP2操作系统下完成KAE虚拟化环境配置后，HostOS中可通过ls -al /sys/class/uacce查询到加速器设备及对应的BDF号，但虚拟机中执行ls /sys/class/uacce/无法查询到设备。虚拟机日志中报错：modprobe: ERROR: could not insert 'hisi hpre': Invalid argument 和 modprobe: ERROR: could not insert 'hisi zip': Invalid argument。

## 问题根因
未对hisi_hpre和hisi_zip设备进行虚拟化配置。

## 解决方案
参考hisi_sec设备的虚拟化配置方法，对hisi_hpre和hisi_zip设备进行相应的虚拟化配置。详细操作步骤请参见《鲲鹏加速库引擎 最佳实践》文档中“KAE在KVM虚拟机中的使用”章节。

