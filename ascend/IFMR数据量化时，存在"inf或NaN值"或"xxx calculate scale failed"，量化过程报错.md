# IFMR数据量化时，存在"inf或NaN值"或"xxx calculate scale failed"，量化过程报错

## 内核版本


## 问题现象
在调用TensorFlow框架执行中间校准模型推理过程中，由于输入数据范围不合法，导致量化算法计算得到的scale不合理，从而校准过程失败，终止校准流程。具体表现为IFMR数据量化时出现inf或NaN值，报错信息包括"Error: Exit Infinite value before data quantization! : Tensor had NaN values"和"xxx calculate scale failed"。

## 问题根因
原始数据不在合法范围内（即超出1/FLT_EPSILON），导致计算出的scale值过大。由于昇腾AI处理器量化采用乘法计算（quantized_value = original_value * scale），当scale大于1/FLT_EPSILON时，1/scale将小于FLT_EPSILON，使得量化结果不可信。因此AMCT量化算法仅支持原始数据范围在1/FLT_EPSILON内进行量化，否则会报错并终止流程。

## 解决方案
根据提示信息，跳过日志中报错的量化层（例如错误信息中提到的Conv_2层），避免对包含inf或NaN值或超出合法范围的数据进行量化。

