# 连接数据库或Master主备倒换异常

## 内核版本


## 问题现象
连接数据库或Master主备倒换异常，出现报错信息：FATAL: remaining connection slots are reserved for non-replication superuser connections。

## 问题根因
数据库“postgresql.conf”配置文件中“max_connections”设置过小。

## 解决方案
1. 使用PuTTY以DonauKit运维用户登录服务器，切换至root账户。
2. 编辑“/usr/local/postgresql/data/postgresql.conf”文件，将“max_connections”修改为大于Donau Scheduler配置连接数的值（例如1000）。
3. 保存并退出编辑。
4. 根据是否为DB HA场景重新加载配置：
   - 非DB HA场景：执行“systemctl reload postgresql.service”。
   - DB HA场景：
     a. 使用“pcs status”确认数据库主节点；
     b. 登录主节点，切换至root再切换至postgres用户；
     c. 执行“pg_ctl reload”重新加载配置。
5. 验证配置是否生效：
   a. 登录数据库节点，切换至postgres用户；
   b. 使用“psql -p 15432”进入数据库控制台（端口号根据实际调整）；
   c. 执行“show max_connections;”确认最大连接数已更新；
   d. 执行“\q”退出数据库。

