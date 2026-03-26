# 使用libaio引擎执行fio测试时osq_lock函数CPU利用率偏高的解决方法

## 内核版本


## 问题现象
使用libaio引擎执行fio测试时，perf top显示内核空间osq_lock函数的CPU利用率超过40%。

## 问题根因
使用kernel rbd方式配合libaio引擎进行测试时，内核路径中osq_lock函数存在较高的CPU占用。

## 解决方案
改用用户态librbd库作为fio的ioengine进行测试，避免进入高开销的内核路径。具体命令为：fio -direct=1 -iodepth=128 -rw=randwrite -ioengine=rbd -bs=4k -numjobs=1 -group_reporting -name=test1 -pool=yourpool -rbdname=imagename。

