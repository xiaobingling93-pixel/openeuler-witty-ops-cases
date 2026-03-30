# Muls算子不支持INT64

## 内核版本


## 问题现象
Muls算子不支持INT64数据类型，导致在使用该算子处理int64类型张量时出现错误。

## 问题根因
Muls算子当前仅支持部分数据类型（如int32），未实现对INT64类型的支持。

## 解决方案
将输入张量的数据类型从int64显式转换为int32，例如将label_batch.npu()修改为label_batch.int().npu()，以规避该问题。

