# Paddle启动训练时报错：Call aclrtGetDevice failed.

## 内核版本


## 问题现象
Paddle启动训练时出现错误：Call aclrtGetDevice failed。

## 问题根因
在创建数据迭代器时未申请新进程，当前CANN 6.0.RC1版本不支持DataLoader的默认参数num_workers=0。

## 解决方案
将DataLoader的num_workers参数设置为大于0的值。

