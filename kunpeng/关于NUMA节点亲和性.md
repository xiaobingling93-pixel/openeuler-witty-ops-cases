# 关于NUMA节点亲和性

## 内核版本


## 问题现象
如何将运行时申请的数组空间分配到不同的NUMA节点中，使核心能够访问自己所在NUMA节点中的内存？

## 问题根因


## 解决方案
有以下两种方法：
1. 通过操作系统提供的numactl命令，制定进程的内存分配策略，例如使用 numactl --membind=<node>。
2. 使用numa库中的numa_all_onnode(size_t size, int node)函数制定NUMA节点上的内存分配策略。

