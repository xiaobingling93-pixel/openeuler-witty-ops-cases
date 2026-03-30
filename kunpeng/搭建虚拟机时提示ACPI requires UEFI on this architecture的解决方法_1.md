# 搭建虚拟机时提示ACPI requires UEFI on this architecture的解决方法

## 内核版本


## 问题现象
搭建虚拟机时，提示“ACPI requires UEFI on this architecture”。

## 问题根因
缺少虚拟机所需的EDK2固件。

## 解决方案
1. 安装EDK2：
   - CentOS 7.6操作系统：执行命令 `yum -y install AAVMF`；
   - CentOS 8.1或openEuler操作系统：执行命令 `yum -y install edk2-aarch64`。
2. 重启libvirtd服务：执行命令 `systemctl restart libvirtd`。

