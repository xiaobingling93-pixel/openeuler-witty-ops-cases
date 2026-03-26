# 启动虚拟机时提示“Permission denied”

## 内核版本


## 问题现象
启动虚拟机时提示“Permission denied”，出现相关错误打印信息。

## 问题根因
原因一：libvirt在执行和访问qemu文件时被AppArmor阻挡，libvirt相关的AppArmor配置出错；原因二：在创建虚拟机时将SELinux临时关闭，导致每次启动虚拟机时提示报错。

## 解决方案
措施一：1. 暂时解除AppArmor对libvirtd的限制（sudo ln -s /etc/apparmor.d/usr.sbin.libvirtd /etc/apparmor.d/disable/）；2. 重新加载libvirtd的AppArmor配置文件（sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.libvirtd）；3. 重启libvirtd服务（systemctl restart libvirtd）。措施二：参考《Atlas 系列硬件产品 虚拟机配置指南》中的“创建虚拟机”章节正确关闭SELinux。

