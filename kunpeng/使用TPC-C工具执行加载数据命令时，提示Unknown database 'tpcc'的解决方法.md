# 使用TPC-C工具执行加载数据命令时，提示Unknown database 'tpcc'的解决方法

## 内核版本


## 问题现象
使用TPC-C工具执行加载数据命令时，提示“Unknown database 'tpcc'”。

## 问题根因
使用TPC-C工具执行数据加载时，指定的数据库'tpcc'不存在。

## 解决方案
1. 在MySQL数据库中创建数据库tpcc：执行命令 mysql -uroot -p123456 -vvv -n < sql/example/mysql/create_database.sql（其中123456为MySQL登录密码，请根据实际情况修改）。
2. 在MySQL数据库中创建数据库表：执行命令 mysql -uroot -p123456 -vvv -n < sql/example/mysql/create_table.sql（密码同样需按实际修改）。
3. 重新执行加载数据命令。

