# virt-manager提示unsupported configuration的解决方法

## 内核版本


## 问题现象
使用virt-manager时，提示错误信息：libvirtError: unsupported configuration: ACPI requires UEFI on this architecture。

## 问题根因
aarch64 KVM只支持UEFI BIOS，编译源码时未安装EDK2，导致无法识别Firmware文件。

## 解决方案
1. 安装EDK2：在CentOS 7.6上执行 'yum -y install AAVMF'；在CentOS 8.1或openEuler上执行 'yum -y install edk2-aarch64'。2. 重启libvirtd服务：执行 'systemctl restart libvirtd'。

