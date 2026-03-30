# K8s集群节点not ready的解决方法

## 内核版本


## 问题现象
节点加入集群后not ready或者节点重启后not ready。

## 问题根因
注释“/etc/fstab”中的swap但未生效。

## 解决方案
通过systemctl禁止交换分区：1. 查看交换分区对应的服务（systemctl | grep swap）；2. 禁止交换分区（systemctl mask dev-sda4.swap）；3. 重启系统（reboot）。

