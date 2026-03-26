# 校准执行过程中提示“[IFMR]: Do layer xxx data calibration failed!”

## 内核版本


## 问题现象
在调用PyTorch框架执行中间校准模型推理过程中，由于输入数据范围不合法，导致量化算法计算得到的scale不合理，从而校准过程失败，终止校准流程。

## 问题根因
原始数据不在合法范围内（即超出±1/FLT_EPSILON），导致AMCT量化算法计算出的scale值过大。由于昇腾AI处理器的量化操作基于乘法（quantized_value = original_value * scale），若scale大于1/FLT_EPSILON，则量化后的结果会小于FLT_EPSILON，失去精度和可信度。因此，AMCT仅支持原始数据在±1/FLT_EPSILON范围内的量化，否则会报错并终止校准。

## 解决方案
根据错误日志提示，跳过报错信息中指定的量化层（例如conv_1层）以规避该问题。

