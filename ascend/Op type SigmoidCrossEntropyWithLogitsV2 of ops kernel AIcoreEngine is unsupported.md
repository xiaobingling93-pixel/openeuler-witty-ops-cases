# Op type SigmoidCrossEntropyWithLogitsV2 of ops kernel AIcoreEngine is unsupported

## 内核版本


## 问题现象
运行时出现错误：Op type SigmoidCrossEntropyWithLogitsV2 of ops kernel AIcoreEngine is unsupported，具体原因为算子SigmoidCrossEntropyWithLogitsV2未在算子库中找到，可能由于输入数据类型（如int64）不被支持。

## 问题根因
SigmoidCrossEntropyWithLogitsV2算子输入了不支持的数据类型，例如int64，导致算子无法在内置或自定义算子库中匹配到对应实现。

## 解决方案
检查并修改Python代码中该算子的输入数据类型，确保使用算子支持的数据类型。

