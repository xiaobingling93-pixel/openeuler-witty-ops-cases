# Multimual算子在动静态编译时行为不一致

## 内核版本


## 问题现象
在PyTorch在线推理场景中，使用相同的输入和模型，固定shape场景下的MultinomialWithReplacement算子可以正常运行，但在动态shape场景下报错，提示该算子不支持。

## 问题根因
问题的根本原因在于动态shape编译时，masked_fill算子的行为异常，导致scores张量中出现大量NaN值，进而使MultinomialWithReplacement算子接收到非法输入（包含负数或NaN），触发其内部的非负校验失败。

## 解决方案
将masked_fill算子的执行设备指定为CPU，规避其在昇腾AI处理器上动态shape编译时的异常行为。

