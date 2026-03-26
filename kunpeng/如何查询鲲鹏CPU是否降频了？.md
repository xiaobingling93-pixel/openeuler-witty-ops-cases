# 如何查询鲲鹏CPU是否降频了？

## 内核版本


## 问题现象
用户希望确认鲲鹏CPU是否因系统负载变化而发生了降频。

## 问题根因
鲲鹏CPU支持ARM的动态频率调节机制，系统会根据当前负载自动调整CPU频率，可能进入节能模式导致频率降低。

## 解决方案
可通过命令 cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq 查看当前CPU频率，确认是否处于降频状态。此外，也可使用 cpufreq-info 命令或检查 /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq 文件获取实时频率信息。若频率始终不变，可尝试在BIOS中将电源策略设置为“Performance”模式以禁用节能降频。

