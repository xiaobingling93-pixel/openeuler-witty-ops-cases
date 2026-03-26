# 删除虚拟机时提示cannot undefine domain with nvram的解决方法

## 内核版本


## 问题现象
执行 virsh undefine vm2 命令时，系统提示错误：error: Requested operation is not valid: cannot undefine domain with nvram。

## 问题根因
虚拟机启动时使用了nvram文件，而销毁该虚拟机时未指定对nvram文件的处理策略，导致无法直接删除虚拟机定义。

## 解决方案
在 virsh undefine 命令中添加 --nvram 参数，以同时删除虚拟机及其对应的nvram文件。具体命令为：virsh undefine vm2 --nvram。

