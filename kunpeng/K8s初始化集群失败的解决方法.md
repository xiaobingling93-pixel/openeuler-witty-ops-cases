# K8s初始化集群失败的解决方法

## 内核版本


## 问题现象
在主节点上进行初始化K8s集群的时候，提示“/proc/sys/net/bridge/bridge-nf-call-iptables contents are not set to 1”问题。

## 问题根因
“/proc/sys/net/bridge/bridge-nf-call-iptables”的值不正确，未设置为1。

## 解决方案
1. 通过命令 echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables 将其置为1；2. 使用 cat /proc/sys/net/bridge/bridge-nf-call-iptables 检查值是否为1；3. 重新执行K8s初始化集群操作。

