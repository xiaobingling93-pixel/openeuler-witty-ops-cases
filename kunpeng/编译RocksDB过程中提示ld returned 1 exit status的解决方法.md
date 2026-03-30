# 编译RocksDB过程中提示ld returned 1 exit status的解决方法

## 内核版本


## 问题现象
编译RocksDB过程中提示“ld returned 1 exit status”。

## 问题根因
在测试之前执行过 make release 编译命令，导致冲突。

## 解决方案
1. 清除上次编译时生成的相关文件：执行 make clean。
2. 再次执行编译命令：make db_stress -j 4。

