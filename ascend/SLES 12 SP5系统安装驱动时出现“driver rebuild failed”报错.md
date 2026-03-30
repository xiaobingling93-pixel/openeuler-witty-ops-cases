# SLES 12 SP5系统安装驱动时出现“driver rebuild failed”报错

## 内核版本
4.12.14-120

## 问题现象
在SLES 12 SP5系统上安装Atlas 300I Pro推理卡或Atlas 300V Pro视频解析卡驱动时，概率性出现安装失败，提示“driver rebuild failed”错误。查看日志文件/var/log/ascend_seclog/ascend_rebuild.log发现大量“fork: retry: No child processes”错误信息。

## 问题根因
SLES系统限定的最大线程数（kernel.pid_max）和systemd服务限定的线程数（DefaultTasksMax）过小，导致驱动编译过程中因多线程资源不足而失败。

## 解决方案
1. 执行命令 sysctl -w kernel.pid_max=131072 修改系统最大线程数，并通过 cat /proc/sys/kernel/pid_max 验证；2. 执行命令 echo DefaultTasksMax=15288 > /etc/systemd/system.conf 修改systemd服务线程限制，并通过 systemctl show --property DefaultTasksMax 验证；3. 重启系统后重新安装驱动。

