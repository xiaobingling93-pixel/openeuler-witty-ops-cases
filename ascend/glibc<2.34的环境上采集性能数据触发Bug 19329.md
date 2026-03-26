# glibc<2.34的环境上采集性能数据触发Bug 19329

## 内核版本


## 问题现象
在安装有glibc<2.34的环境上进行性能数据采集时，触发core dumped。

## 问题根因
该问题由glibc版本低于2.34时存在的Bug 19329引起，具体可参考https://sourceware.org/bugzilla/show_bug.cgi?id=19329。

## 解决方案
通过升级环境的glibc版本至2.34或更高可解决此问题。

