# 搭建MySQL+MGR单主模式过程中，提交事务时提示存在的事务过多的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，执行START GROUP_REPLICATION;后提示“This member has more executed transactions than those present in the group”。

## 问题根因
可能是因为数据不同步导致的问题。

## 解决方案
1. 重置master服务并查询master状态，执行reset master; show master status\G；2. 重新执行START GROUP_REPLICATION;以启动MySQL Group Replication插件。

