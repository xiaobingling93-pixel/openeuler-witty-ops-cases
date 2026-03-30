# 搭建MySQL+MGR单主模式时提示--super-read-only选项正在使用的解决方法

## 内核版本


## 问题现象
搭建MySQL 8.0.18+MGR单主模式过程中，执行 alter user 'repl'@'%' IDENTIFIED WITH caching_sha2_password; 后提示“The MySQL server is running with the --super-read-only option so it cannot execute this statement”。

## 问题根因
主库设置了只读模式（--super-read-only），导致无法执行需要写权限的SQL语句。

## 解决方案
1. 关闭主库的只读模式：set global read_only=OFF; 
2. 重新执行原命令：alter user 'repl'@'%' IDENTIFIED WITH caching_sha2_password;

