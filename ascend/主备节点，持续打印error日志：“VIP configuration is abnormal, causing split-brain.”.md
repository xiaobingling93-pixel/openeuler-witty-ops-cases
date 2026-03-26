# 主备节点，持续打印error日志：“VIP configuration is abnormal, causing split-brain.”

## 内核版本


## 问题现象
使用KEEPALIVED部署双机备份后，容器运行异常，查看/var/log/keepalived/下的日志，持续提示error日志：“VIP configuration is abnormal, causing split-brain.”。

## 问题根因
存在以下两种可能原因：1. VRRP被iptables禁用；2. 在HA正常运行过程中，第三台边缘设备（非主备节点）上配置了相同的浮动IP/VIP，导致脑裂。

## 解决方案
针对原因1：以root用户登录主备节点，执行命令 iptables -A INPUT -p vrrp -j ACCEPT 和 iptables -A OUTPUT -p vrrp -j ACCEPT 以允许VRRP协议通信。针对原因2：1. 在HA组任意节点执行 arping -I eth4 192.168.65.73（替换为实际业务网卡和VIP），查找不属于HA组的MAC地址；2. 登录对应设备，通过 ip addr | grep 192.168.65.73 确认VIP配置；3. 执行 ip -f inet addr del 192.168.65.73 dev eth0（替换为实际网卡）删除非法VIP配置。

