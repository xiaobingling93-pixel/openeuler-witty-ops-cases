# 编译PostgreSQL时提示conflicting types for copy_file_range的解决方法

## 内核版本


## 问题现象
在ARM服务器编译PostgreSQL 10.1及以上版本时，出现错误：copy_fetch.c:159:1: error: conflicting types for 'copy_file_range'。原因是系统头文件/usr/include/unistd.h中已声明了copy_file_range函数（Linux 4.5引入的系统调用），而PostgreSQL源码中又自定义了同名函数，导致类型冲突。

## 问题根因
copy_file_range是Linux 4.5引入的系统调用，在较旧的Linux系统中并不支持该调用。但在某些系统环境中，即使内核版本较低，glibc可能已提前声明了该函数，而PostgreSQL源码中又自行实现了同名函数，造成函数签名不一致的冲突。

## 解决方案
将PostgreSQL源码中src/bin/pg_rewind/copy_fetch.c文件内的自定义函数copy_file_range重命名为copy_file_chunk，避免与系统声明的函数冲突。具体操作为执行命令：sed -i "s/copy_file_range/copy_file_chunk/g" src/bin/pg_rewind/copy_fetch.c，然后重新编译安装PostgreSQL（make && make install）。

