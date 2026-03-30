# 执行Aicore压测时，进程被killed，导致进程异常终止

## 内核版本


## 问题现象
执行aicore压测时，进程被killed，导致进程异常终止。

## 问题根因
进程使用的内存超过内存上限，触发系统OOM killer机制，导致进程被强制终止。通过查看OS系统日志（/var/log/message或/var/log/syslog）可发现oom-killer相关日志，并可确认进程所属cgroup组及其内存限制信息。

## 解决方案
1. 在执行压测命令前预留足够内存，防止因内存不足导致进程被杀；2. 调整进程所在cgroup组的内存上限阈值，可通过/sys/fs/cgroup/memory/${进程运行的cgroup}/memory.limit_in_bytes（cgroup v1）或memory.max（cgroup v2）进行配置。

