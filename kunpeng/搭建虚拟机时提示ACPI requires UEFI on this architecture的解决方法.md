# 搭建虚拟机时提示ACPI requires UEFI on this architecture的解决方法

## 内核版本


## 问题现象
搭建虚拟机时，提示“ACPI requires UEFI on this architecture”。

## 问题根因
缺少虚拟机需要的依赖库。

## 解决方案
安装虚拟机依赖库。执行命令：yum install AAVMF.noarch qemu-kvm* libvirt* virt-install*

