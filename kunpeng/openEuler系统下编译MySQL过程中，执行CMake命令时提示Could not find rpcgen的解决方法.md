# openEuler系统下编译MySQL过程中，执行CMake命令时提示Could not find rpcgen的解决方法

## 内核版本


## 问题现象
在openEuler系统下编译MySQL过程中，执行CMake命令时提示：CMake Error at plugin/group_replication/libmysqlgcs/rpcgen.cmake:100 (MESSAGE): Could not find rpcgen。

## 问题根因
缺失rpcsvc软件包，rpcgen是生成RPC协议代码的工具，而rpcsvc是rpcgen所依赖的软件包之一。

## 解决方案
1. 下载rpcsvc安装包：wget https://github.com/thkukuk/rpcsvc-proto/releases/download/v1.4/rpcsvc-proto-1.4.tar.gz；2. 解压安装包：tar -zxvf rpcsvc-proto-1.4.tar.gz；3. 编译安装：./configure && make && make install；4. 重新执行CMake命令。

