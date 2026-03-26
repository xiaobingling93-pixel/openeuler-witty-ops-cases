# 安装environment-modules依赖后，如何使用module命令？

## 内核版本


## 问题现象
安装environment-modules依赖后，无法直接使用module命令。

## 问题根因
未加载modules环境变量脚本，导致module命令不可用。

## 解决方案
根据操作系统类型执行对应的环境变量加载命令：Ubuntu系统运行 source /usr/share/modules/init/bash；其他操作系统运行 source /usr/share/Modules/init/bash。

