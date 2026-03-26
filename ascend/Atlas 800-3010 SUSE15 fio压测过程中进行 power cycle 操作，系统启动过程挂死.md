# Atlas 800-3010 SUSE15 fio压测过程中进行 power cycle 操作，系统启动过程挂死

## 内核版本
4.12.14-23-default

## 问题现象
在SLES 15系统上对非系统分区进行fio性能测试时，执行power cycle操作后，系统在启动过程中挂死。串口日志显示内核发生Oops并触发Kernel panic，错误信息为'BUG: unable to handle kernel paging request at ffffffffffffffff'，最终提示'Attempted to kill the idle task!'。

## 问题根因
该问题是由于内核efi模块的已知缺陷导致，在内核版本4.12.14-150.14.2.x86_64中已修复。

## 解决方案
下载并安装内核补丁kernel-default-4.12.14-150.14.2.x86_64.rpm，升级内核以解决问题。

