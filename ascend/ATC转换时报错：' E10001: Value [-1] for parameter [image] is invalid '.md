# ATC转换时报错：' E10001: Value [-1] for parameter [image] is invalid '

## 内核版本


## 问题现象
执行ATC模型转换时，报错'E10001: Value [-1] for parameter [image] is invalid'。

## 问题根因
通过报错信息确定是--input_shape参数有问题。使用netron软件打开该ONNX模型后发现，--input_shape参数中指定的输入名称错误，应为'image'而非'images'，导致参数值无效。

## 解决方案
将--input_shape参数修改为正确的输入名称和形状，本案例中应改为--input_shape="image:1,3,224,224"。

