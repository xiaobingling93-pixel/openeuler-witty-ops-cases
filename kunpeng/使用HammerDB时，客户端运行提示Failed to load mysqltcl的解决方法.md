# 使用HammerDB时，客户端运行提示Failed to load mysqltcl的解决方法

## 内核版本


## 问题现象
使用HammerDB工具时，客户端运行提示“Failed to load mysqltcl”。

## 问题根因
“/usr/local/lib64”目录下缺少HammerDB所需的库文件。

## 解决方案
1. 将数据库安装路径的libmysqlclient*拷贝到“/usr/local/lib64”目录下（例如：cp /usr/local/mysql-8.0.20-tpch/lib/libmysqlclient.so /usr/local/lib64/）；2. 将GCC版本升级为7.3.0。

