# 搭建MySQL+MGR单主模式时提示binlog校验和应为NONE的解决方法

## 内核版本


## 问题现象
在搭建MySQL 8.0.18+MGR单主模式过程中，执行install PLUGIN group_replication SONAME 'group_replication.so';语句安装MGR插件时，系统提示“binlog_checksum should be NONE for Group Replication”和“Unable to start Group Replication on boot”。

## 问题根因
MGR插件在MySQL 5.7之前的版本不支持binlog_checksum，若该参数被设置为非NONE值会导致插件无法正常工作。尽管当前使用的是MySQL 8.0.18（高于5.7），但系统仍要求显式将binlog_checksum设为NONE以兼容MGR插件的启动条件。

## 解决方案
1. 在MySQL配置文件的[mysqld]段落下添加或修改参数：binlog_checksum=none；2. 重启MySQL服务（例如执行sudo service mysql restart）；3. 重新执行安装MGR插件的命令：install PLUGIN group_replication SONAME 'group_replication.so';

