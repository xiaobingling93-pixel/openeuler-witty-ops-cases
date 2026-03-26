# 物理机下电再上电后OpenStack虚拟机启动失败

## 内核版本


## 问题现象
在OpenStack集成Ceph场景下，物理机强制下电或异常下电再重新上电后，虚拟机无法正常启动。虚拟机console日志和libvirt日志显示连接后端块存储异常。

## 问题根因
异常断电导致虚拟机与后端Ceph RBD块存储的连接状态异常，使得虚拟机重启时无法正确挂载其磁盘卷。

## 解决方案
1. 使用nova show $vm_id获取虚拟机实例名称instance_name；2. 通过virsh dumpxml $instance_name | grep -w source获取RBD卷名rbd_name；3. 执行rbd map $rbd_name和rbd unmap $rbd_name重新挂载并卸载该卷以恢复连接状态；4. 最后执行nova reboot $vm_id重启虚拟机即可恢复正常。

