# 使用IVFSQT算法时，update接口报错

## 内核版本


## 问题现象
在Atlas推理系列产品环境中，使用IVFSQT算法调用update接口时出现报错。

## 问题根因
使用setThreshold接口设置threshold参数时，参数值设置过大，导致Device侧内存使用超过限额，触发OOM机制，进程被杀死。

## 解决方案
在Atlas推理系列产品环境中使用IVFSQT算法时，应先查看Device侧内存限额（/sys/fs/cgroup/memory/usermemory/memory.limit_in_bytes），合理评估底库大小，建议将threshold参数值设置在[1.0, 1.1]范围内。

