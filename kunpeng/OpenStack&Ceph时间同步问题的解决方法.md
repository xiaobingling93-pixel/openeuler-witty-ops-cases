# OpenStack&Ceph时间同步问题的解决方法

## 内核版本


## 问题现象
Ceph+OpenStack的集群时间不同步导致部分服务无法正常运行。

## 问题根因
Ceph+OpenStack的集群环境中，节点之间的时间差异较大，导致产生告警，Cinder以及Cinder_backup组件可能出现部分服务故障。

## 解决方案
1. 在所有节点上同时执行date命令，检查各个节点时间是否与控制节点时间一致。2. 在时间不一致的节点上执行如下命令重新启用NTP时间同步：timedatectl set-ntp no; timedatectl set-ntp yes。

