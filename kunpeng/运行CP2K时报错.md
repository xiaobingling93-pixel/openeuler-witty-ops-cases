# 运行CP2K时报错

## 内核版本


## 问题现象
运行cp2k.psmp时报错，报错信息为：“mpirun noticed that process rank 0 with PID 0 on node XA320V2-90 exited on signal 11 (Segmentation fault)”。

## 问题根因
软件对容量要求太高，导致内存资源不够。

## 解决方案
更换比较小的软件自带测试算例或者增加内存容量。

