# 主备节点，持续打印error日志：“VIP disappears!”

## 内核版本


## 问题现象
使用KEEPALIVED部署双机备份后，容器运行异常，查看/var/log/keepalived/下的日志，持续提示error日志：“VIP disappears!”。适用于MindX Edge 3.0.0及以下版本。

## 问题根因
心跳网卡故障或者连接心跳网卡的网线松动/断开。

## 解决方案
1. 检查心跳网卡是否存在故障；2. 检查连接心跳网卡的网线是否松动或断开，如有问题则重新连接，并重启主备节点的KEEPALIVED容器。

