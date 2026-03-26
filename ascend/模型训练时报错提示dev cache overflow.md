# 模型训练时报错提示dev cache overflow

## 内核版本


## 问题现象
使用Rec SDK进行模型训练时，报错提示“dev cache overflow”。

## 问题根因
模型中“dev_vocab_size”参数值设置过小。

## 解决方案
修改模型中的“dev_vocab_size”参数（device vocabulary size），适当调大该值。注意值过大会导致设备侧出现out of memory错误，应根据实际训练情况和设备HBM存储大小合理调整。

