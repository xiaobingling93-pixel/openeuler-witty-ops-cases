# Atlas 800-3010 Debian 9.9在第二内核加nr_cpus=8后，kdump测试失败

## 内核版本


## 问题现象
Atlas 800-3010 Debian 9.9系统在第二内核启动参数中添加nr_cpus=8后，进行kdump测试时系统突然宕机，未能生成vmcore文件。

## 问题根因
fio压力测试超过磁盘处理能力极限，导致IO处理流程过长，最终触发softlockup，使系统崩溃且无法完成kdump。

## 解决方案
针对fio压测场景，需延长softlockup触发时间并关闭softlockup panic：临时修改可通过sysctl命令设置kernel.watchdog_print_period=60、kernel.watchdog_thresh=30、kernel.softlockup_panic=0；永久修改需将上述参数写入/etc/sysctl.conf并执行sysctl -p生效。

