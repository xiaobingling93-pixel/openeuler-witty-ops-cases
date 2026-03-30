# 搭建MySQL+MGR单主模式时，提示身份验证不安全的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，执行START GROUP_REPLICATION;后提示“Authentication requires secure connection”。

## 问题根因
MySQL 8.0默认使用caching_sha2_password身份验证机制，如果使用默认身份验证机制创建用户，在后续连接远程节点时会抛错。

## 解决方案
将原来的mysql_native_password更改为caching_sha2_password。在数据库中执行如下语句：SET SQL_LOG_BIN=0; alter user 'repl'@'%' IDENTIFIED WITH mysql_native_password BY 'password'; GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%' ; SET SQL_LOG_BIN=1; 然后重新执行START GROUP_REPLICATION;

