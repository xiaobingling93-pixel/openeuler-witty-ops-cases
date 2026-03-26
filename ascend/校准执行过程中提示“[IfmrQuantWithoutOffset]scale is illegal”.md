# 校准执行过程中提示“[IfmrQuantWithoutOffset]scale is illegal”

## 内核版本


## 问题现象
在调用ONNX Runtime框架执行中间校准模型推理过程中，由于输入数据范围不合法，导致量化算法计算得到的scale值过大（大于1/FLT_EPSILON），从而触发错误提示“[IfmrQuantWithoutOffset]scale is illegal”，校准流程失败并终止。

## 问题根因
原始输入数据范围超出了合法区间[-1/FLT_EPSILON, 1/FLT_EPSILON]，导致量化算法计算出的scale值过大。昇腾AI处理器在量化时使用乘法运算（quantized_value = original_value * scale），若scale大于1/FLT_EPSILON，则1/scale将小于FLT_EPSILON，使得量化结果不可信，因此AMCT量化算法拒绝此类scale并报错。

## 解决方案
根据错误日志中提示的量化层（如batchmatmul_7），在量化配置中跳过这些层，避免对不合法数据范围的层进行量化。

