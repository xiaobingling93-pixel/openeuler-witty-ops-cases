# 使用insmod tzdriver加载驱动后，为什么tzdriver卸载不掉？

## 内核版本


## 问题现象
使用insmod命令加载tzdriver驱动后，无法通过rmmod等常规方式卸载该驱动。

## 问题根因
tzdriver驱动在设计上不支持运行时卸载，一旦加载，必须通过服务器完全重启才能释放相关资源。

## 解决方案
如需卸载tzdriver，必须重启服务器。

