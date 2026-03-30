# OM模型推理报错，报错码EH9999，ctx is NULL

## 内核版本


## 问题现象
使用Python装饰器封装推理代码后，运行时报错，错误码为EH9999，关键错误信息为“ctx is NULL”。

## 问题根因
在推理过程中Context未正确创建，问题出现在装饰器的闭包结构中未正确传递或初始化Context。

## 解决方案
需要将Context作为参数传入装饰器函数，或在装饰器内部显式调用acl.rt.create_context(device_id)创建Context以便管理。

