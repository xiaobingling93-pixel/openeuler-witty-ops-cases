# 校准执行过程中提示"IfmrQuantCalibration with offset scale is illegal"或"IfmrQuantCalibration without offset scale is illegal"

## 内核版本


## 问题现象
在调用Caffe框架执行中间校准模型推理过程中，由于输入数据范围不合法（如包含无穷大值或超出支持的浮点精度范围），导致量化算法计算得到的scale不合理（如为+inf或大于1/FLT_EPSILON），从而触发错误信息"IfmrQuantCalibration with offset scale is illegal"或"IfmrQuantCalibration without offset scale is illegal"，校准流程失败并终止。

## 问题根因
AMCT量化算法要求输入数据范围必须合法。一方面，若数据范围包含[-inf, +inf]，由于算法强制过零点，会导致计算出的scale为inf，无法用于后续量化；另一方面，若数据范围过大导致计算出的scale大于1/FLT_EPSILON，则量化后的结果不可信。这两种情况均被算法判定为非法，从而报错终止校准。

## 解决方案
根据日志中提示的错误信息，跳过报错的量化层（例如Convolution1层）进行校准。

