# 创建虚拟机失败，日志提示libvirtError的解决方法

## 内核版本


## 问题现象
使用OpenStack创建虚拟机失败，日志提示“libvirtError”。

## 问题根因
服务器支持virt_type为KVM，而不是QEMU，当选择了QEMU时，就无法创建虚拟机。

## 解决方案
1. 修改nova配置文件“/etc/nova/nova.conf”，在[libvirt]字段下的virt_type配置为：

   virt_type = kvm

2. 重启nova-compute服务使配置生效：

   systemctl restart openstack-nova-compute.service

