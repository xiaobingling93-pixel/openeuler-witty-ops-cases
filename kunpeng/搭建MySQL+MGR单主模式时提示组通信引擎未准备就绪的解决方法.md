# 搭建MySQL+MGR单主模式时提示组通信引擎未准备就绪的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，执行START GROUP_REPLICATION;语句后提示“The group communication engine is not ready for the member to join”。

## 问题根因
第一次启动组复制时，未将group_replication_bootstrap_group设置为ON。

## 解决方案
1. 在主节点上执行SET GLOBAL group_replication_bootstrap_group=ON; 2. 重新执行START GROUP_REPLICATION;启动MySQL Group Replication；3. 启动成功后，执行SET GLOBAL group_replication_bootstrap_group=OFF;恢复配置。

