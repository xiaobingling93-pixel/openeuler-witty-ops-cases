# 使用BenchMarkSQL测试MySQL过程中提示java.lang.OutOfMemoryError的解决方法

## 内核版本


## 问题现象
使用BenchMarkSQL测试MySQL过程中，提示“java.lang.OutOfMemoryError: Java heap space”和“java.lang.OutOfMemoryError: GC overhead limit exceeded”。

## 问题根因
可能是因为分配的内存太小，同时MySQL的my.cnf文件中innodb_buffer_pool_size（Buffer Pool）配置值过大，导致Java进程内存不足。

## 解决方案
合理配置MySQL的innodb_buffer_pool_size参数，建议设置为系统内存的60%～70%。例如在32GB内存的KVM虚拟机中，可设为20GB；若开启performance_schema，则建议设为18GB。可通过修改my.cnf配置文件（需重启MySQL）或执行SQL命令“SET GLOBAL innodb_buffer_pool_size = <size_in_bytes>;”动态调整。调整后重新执行测试任务。

