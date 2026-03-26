# 启动KVM虚拟机提示seccomp support is disabled的解决方法

## 内核版本


## 问题现象
鲲鹏服务器基于CentOS 7.6安装KVM虚拟机，在libvirt和QEMU升级后，创建虚拟机安装OS时提示“seccomp support is disabled”。

## 问题根因
因为安装了libseccomp库，libvirt默认seccomp特性是打开的，但实际编译安装QEMU时未启用seccomp特性。

## 解决方案
升级QEMU之前，需要先安装libseccomp devel依赖包，执行命令：yum install libseccomp-devel。

