# KVM连接Hypervisor时异常的解决方法

## 内核版本


## 问题现象
连接Hypervisor后，执行 virsh version 命令时出现错误：error: failed to connect to the hypervisor；error: Failed to connect socket to '/var/run/libvirt/libvirt-sock': No such file or directory。

## 问题根因
libvirtd服务未启动，导致无法创建或找到 /var/run/libvirt/libvirt-sock 套接字文件。

## 解决方案
1. 重启libvirtd服务：service libvirtd restart；2. 再次执行 virsh version 验证连接是否恢复正常，预期输出包括libvirt和QEMU的版本信息。

