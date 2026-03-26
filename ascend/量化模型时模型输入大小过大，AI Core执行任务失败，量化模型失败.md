# 量化模型时模型输入大小过大，AI Core执行任务失败，量化模型失败

## 内核版本


## 问题现象
在使用atc工具进行模型量化转换时，指定的input_shape参数中Batch size值过大（如64），导致AI Core执行任务失败，报错信息包括'Aicore kernel execute failed'和'execute model failed, errorCode is 507011'等，最终量化过程失败。

## 问题根因
input_shape参数中指定的Batch size值过大，超出了AI Core硬件资源的处理能力，导致算子执行失败。

## 解决方案
将input_shape参数中的Batch size值调小（例如从64调整为8），然后重新执行模型转换命令。

