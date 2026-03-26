# 查看MySQL主从复制状态时提示The slave IO thread stops的解决方法

## 内核版本


## 问题现象
登录从库，查看从库状态时，提示“The slave I/O thread stops because master and slave have equal MySQL server UUIDs; these UUIDs must be different for replication to work.”

## 问题根因
在MySQL主从复制架构中，主库和从库的MySQL实例具有相同的server UUID。该UUID存储在datadir目录下的auto.cnf文件中，若主从实例UUID相同，则会导致复制失败。

## 解决方案
1. 先关闭从库，再关闭主库。
2. 在主库和从库上分别删除data目录下的auto.cnf文件（路径示例：/data/mysql/data/auto.cnf）。
3. 先启动主库，再启动从库。
4. 登录从库，执行“start slave;”命令启动复制进程。
5. 执行“SHOW SLAVE STATUS;”确认主从复制状态恢复正常。

