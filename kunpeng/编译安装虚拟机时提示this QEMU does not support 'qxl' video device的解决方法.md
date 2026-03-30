# 编译安装虚拟机时提示this QEMU does not support 'qxl' video device的解决方法

## 内核版本


## 问题现象
在编译安装虚拟机时，未启用SPICE，导致安装过程中提示错误信息："this QEMU does not support 'qxl' video device"。

## 问题根因
QEMU编译安装时未启用SPICE支持，而'qxl'视频设备依赖SPICE功能。

## 解决方案
在执行./configure命令时添加--enable-spice参数，以启用SPICE支持。

