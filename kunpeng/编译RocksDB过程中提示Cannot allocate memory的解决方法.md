# 编译RocksDB过程中提示Cannot allocate memory的解决方法

## 内核版本


## 问题现象
编译RocksDB过程中提示“Cannot allocate memory”。

## 问题根因
执行 make -j 编译RocksDB时，会使用所有CPU核数，导致内存不足。

## 解决方案
1. 删除当前目录下的所有文件和子目录（rm -rf *）。
2. 使用CMake工具编译安装RocksDB数据库，并指定安装路径为“/usr/local/rocksdb”（可根据实际情况修改）：cmake -DCMAKE_INSTALL_PREFIX=/usr/local/rocksdb -DWITH_SNAPPY=1 -DWITH_ZLIB=1 -DWITH_LZ4=1 -DWITH_ZSTD=1 -DWITH_BZ2=1 ..
3. 查看CPU核数（lscpu）。
4. 再次执行编译命令，同时减少使用的CPU核数，例如：make -j 8。

