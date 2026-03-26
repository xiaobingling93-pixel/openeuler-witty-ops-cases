# 搭建MySQL+MGR单主模式时，提示Gtid模式应为ON的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，执行START GROUP_REPLICATION;后提示“Gtid mode should be ON for Group Replication”。

## 问题根因
GTID是一个全局唯一的标识符，用于跟踪在分布式系统中的事务。搭建MGR需要开启GTID，但当前GTID模式未开启。

## 解决方案
1. 启用和配置MySQL GTID：依次执行以下命令：set global enforce_gtid_consistency=ON; set global gtid_mode=OFF_PERMISSIVE; set global gtid_mode=ON_PERMISSIVE; set global gtid_mode=ON; 2. 重新执行START GROUP_REPLICATION;以启动MySQL Group Replication。

