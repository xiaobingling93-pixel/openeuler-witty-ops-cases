# 安装Hyper MPI执行make命令报 'limits' file not found？错误信息时如何处理？

## 内核版本


## 问题现象
安装Hyper MPI执行make命令时提示 'limits' file not found 错误。

## 问题根因
系统中缺少 limits.h 头文件，或环境变量 INCLUDE 未包含 /usr/include 目录。

## 解决方案
1. 检查环境变量 INCLUDE 是否包含 '/usr/include'：执行 'echo $INCLUDE'；若包含，则继续下一步，否则联系设备厂家。2. 检查 '/usr/include' 目录下是否存在 limits.h 文件：执行 'll /usr/include | grep limits.h'；若存在，联系华为技术支持；若不存在，联系设备厂家。

