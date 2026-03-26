# 生成算子时ATC报错

## 内核版本


## 问题现象
生成距离算子时，ATC出现报错：Call InferShapeAndType for nodeXXXX failed。

## 问题根因
新版CANN加强了校验，InferDataType实现不可缺少。

## 解决方案
设置环境变量 export IGNORE_INFER_ERROR=1 进行规避。

