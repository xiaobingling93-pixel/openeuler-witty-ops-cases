# 编译安装MySQL过程中，执行CMake命令失败的解决方法

## 内核版本


## 问题现象
在编译安装MySQL过程中，执行CMake命令时失败，并提示错误信息（见图1）：cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/data/mysql -DSYSCONFDIR=/etc -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DWITH_FEDERATED_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_MYISAM_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DENABLE_DTRACE=0 -DDEFAULT_CHARSET=utf8mb4 -DDEFAULT_COLLATION=utf8mb4_general_ci -DWITH_EMBEDDED_SERVER=1 -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/home/mysql-5.7.27/boost/boost_1_59_0。错误信息显示与CMake缓存相关的问题。

## 问题根因
在MySQL源码根目录下曾经执行过cmake命令，导致生成了CMakeCache.txt文件。该文件的存在干扰了后续的cmake配置过程，从而引发错误。

## 解决方案
删除源码目录下的CMakeCache.txt文件后重新执行cmake命令。具体步骤为：1. 进入MySQL源码目录（如 /home/mysql-5.7.27）并删除CMakeCache.txt：`cd /home/mysql-5.7.27 && rm CMakeCache.txt`；2. 重新运行原cmake命令进行配置。

