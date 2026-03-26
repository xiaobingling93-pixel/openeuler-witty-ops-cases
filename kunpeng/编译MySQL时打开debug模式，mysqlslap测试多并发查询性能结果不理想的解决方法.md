# 编译MySQL时打开debug模式，mysqlslap测试多并发查询性能结果不理想的解决方法

## 内核版本


## 问题现象
在鲲鹏服务器、中标麒麟7.6操作系统环境下，使用从官网下载的mysql-boost-5.7.21.tar.gz编译安装MySQL后，通过mysqlslap进行多并发查询性能测试，发现测试结果不理想。

## 问题根因
编译MySQL时在cmake命令中启用了“-DWITH_DEBUG=1”选项，导致MySQL运行在debug模式下。与release模式相比，debug模式因包含额外的调试信息和检查逻辑，显著降低了性能，从而影响了mysqlslap的多并发查询测试结果。

## 解决方案
在cmake编译命令中移除“-DWITH_DEBUG=1”选项，改用release模式重新编译安装MySQL。具体命令为：cmake -DBUILD_CONFIG=mysql_release -DCMAKE_INSTALL_PREFIX=/data1/xk/mysql_3306 -DMYSQL_TCP_PORT=3306 -DWITH_BOOST=../boost/ ..

