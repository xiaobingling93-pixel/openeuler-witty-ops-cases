# 日志权限有问题导致Ascend DMI功能不可用

## 内核版本


## 问题现象
使用Ascend DMI工具时报错，提示'The log is abnormal. Check the log status'。

## 问题根因
日志文件或目录的权限或属组不满足要求。

## 解决方案
根据用户类型调整日志文件权限：root用户的日志路径为/var/log/ascend-dmi，非root用户为~/var/log/ascend-dmi。执行chmod 600命令修改日志文件权限，例如：chmod 600 /var/log/ascend-dmi/ascend-dmi-operation.log 和 chmod 600 /var/log/ascend-dmi/ascend-dmi.log。

