# 使用训练后量化进行量化时，量化过程存在空tensor输入报错信息

## 内核版本


## 问题现象
执行训练后量化时，出现多次 '[ERROR][QuantIfmrInternelGpu][114] Empty pointer, all input tensor is empty' 报错信息。

## 问题根因
输入数据不是真实数据集，导致量化过程中输入的tensor为空。

## 解决方案
请使用真实数据集进行训练后量化。

