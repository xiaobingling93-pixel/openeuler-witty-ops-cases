# 将鲲鹏节点加入主从复制部署过程中提示ERROR 1872

## 内核版本


## 问题现象
将鲲鹏节点加入主从复制部署过程中，执行SQL语句 start slave; 启动鲲鹏从库的复制进程时，提示 ERROR 1872 (HY000): Replica failed to initialize applier metadata structure from the repository。

## 问题根因
从库连接到主库过程中存在误操作（例如没有将“gtid_mode”设置为“ON”），导致主从关系建立失败。再次尝试建立主从关系时，需要重置从库的复制元数据。

## 解决方案
1. 执行 reset slave; 重置从库配置。
2. 重新执行 start slave; 启动鲲鹏从库的复制进程。

