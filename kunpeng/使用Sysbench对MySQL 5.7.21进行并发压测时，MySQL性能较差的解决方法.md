# 使用Sysbench对MySQL 5.7.21进行并发压测时，MySQL性能较差的解决方法

## 内核版本


## 问题现象
使用Sysbench对MySQL 5.7.21进行256并发压测时，鲲鹏920处理器下TPS为4197，显著低于x86平台下的TPS 10685，性能差距明显。

## 问题根因
MySQL热点函数MVCC::view_open和PolicyMutex_在底层调用spin_lock相关函数，导致大量线程自旋空转，系统调用占比高，CPU资源消耗大；此外，MySQL源码中硬编码的CacheLine大小（64字节）与鲲鹏920处理器的实际CacheLine大小（128字节）不匹配，进一步影响性能。

## 解决方案
1. （可选）修改MySQL源码中CacheLine大小以适配鲲鹏920处理器的128字节CacheLine；2. 调整MySQL配置参数：将innodb_thread_concurrency设为CPU核心数，适当上调innodb_spin_wait_delay和innodb_sync_spin_loops，通过perf top监控热点函数使用率直至降至合理范围，从而优化自旋锁性能。

