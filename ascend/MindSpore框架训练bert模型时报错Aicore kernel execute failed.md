# MindSpore框架训练bert模型时报错Aicore kernel execute failed

## 内核版本


## 问题现象
MindSpore框架训练bert模型时出现错误：Aicore kernel execute failed，具体信息包括device_id=0, stream_id=19, task_id=23，故障算子名为gather_v2_d_14414100058973704710_0__kernel0。

## 问题根因
自定义模块中的3个Embedding操作的vocab_size参数值小于输入x中的元素最大值，导致gather_v2算子接收到不符合要求的数据，从而引发Aicore kernel执行失败。

## 解决方案
将bert_model.py文件中这三个Embedding操作的vocab_size参数修改为配置文件config中指定的正确大小，确保vocab_size不小于输入数据中的最大索引值。

