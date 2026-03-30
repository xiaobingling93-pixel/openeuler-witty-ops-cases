# 对紫东太初模型的视觉问答任务进行微调时，出现“' NoneType' object has no atribute 'shape'. ”

## 内核版本


## 问题现象
对紫东太初大模型的视觉问答任务进行微调时，出现“' NoneType' object has no attribute 'shape'”错误。

## 问题根因
MindSpore框架默认启用了JIT Callback（文中称为JIT Fallback）特性，导致在处理某些数据时返回None，从而引发NoneType对象没有shape属性的错误。

## 解决方案
通过设置环境变量关闭JIT Fallback特性：export MS_DEV_ENABLE_FALLBACK=0。

