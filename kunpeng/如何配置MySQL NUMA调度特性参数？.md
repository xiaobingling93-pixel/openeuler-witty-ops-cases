# 如何配置MySQL NUMA调度特性参数？

## 内核版本


## 问题现象
MySQL在OLTP高并发场景下，系统默认的线程调度导致用户处理线程频繁跨NUMA节点访问内存，造成CPU开销增大、性能受限；同时后台线程也存在跨NUMA访问问题，影响执行效率。

## 问题根因
Linux系统默认的线程调度策略未针对NUMA架构进行优化，导致MySQL工作线程和后台线程在运行过程中频繁访问远程NUMA节点的内存，引发较高的内存访问延迟和CPU资源浪费。

## 解决方案
通过应用MySQL NUMA调度Patch，对用户处理线程进行动态绑定到特定NUMA节点的CPU（如设置sched_affinity_foreground_thread参数为'2-5'等），减少跨NUMA访问；同时将后台线程静态绑定到固定NUMA节点CPU。参数可通过配置文件、启动参数或运行时SQL命令（如set global sched_affinity_foreground_thread = '2-5';）进行设置。

