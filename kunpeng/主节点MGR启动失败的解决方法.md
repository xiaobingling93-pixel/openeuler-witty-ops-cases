# 主节点MGR启动失败的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，主节点MGR启动失败，执行START GROUP_REPLICATION;后提示“Error on opening a connection to 192.168.102.175:33061 on local port: 33061”。

## 问题根因
第一次启动组复制时，未将group_replication_bootstrap_group设置为ON。

## 解决方案
1. 在主节点上执行 SET GLOBAL group_replication_bootstrap_group=ON; 2. 重新执行 START GROUP_REPLICATION; 启动MySQL Group Replication；3. 恢复配置 SET GLOBAL group_replication_bootstrap_group=OFF;

