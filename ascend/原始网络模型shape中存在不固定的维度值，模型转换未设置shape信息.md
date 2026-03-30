# 原始网络模型shape中存在不固定的维度值，模型转换未设置shape信息

## 内核版本


## 问题现象
执行模型转换命令时提示E10001报错：Value [-1] for parameter [Inputs] is invalid. Reason: maybe you should set input_shape to specify its shape。

## 问题根因
原始模型的输入shape中包含不固定的维度值“-1”，在模型转换过程中未通过input_shape参数指定该维度的具体值或范围。

## 解决方案
可通过以下任一方式解决：1) 设置固定shape，如--input_shape="Inputs:1,224,224,3"；2) 设置shape分档配合dynamic_batch_size参数，如--input_shape="Inputs:-1,224,224,3" --dynamic_batch_size="1,2,4,8"；3) 设置shape范围，如--input_shape="Inputs:1~10,224,224,3"。

