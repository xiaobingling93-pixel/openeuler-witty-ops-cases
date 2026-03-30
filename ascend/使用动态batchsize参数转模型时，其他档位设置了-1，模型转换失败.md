# 使用动态batchsize参数转模型时，其他档位设置了-1，模型转换失败

## 内核版本


## 问题现象
使用ATC工具进行模型转换时，若使用--dynamic_batch_size参数且在--input_shape中将非Batch维度（如H、W）也设置为-1，则会报错E10018，提示“Value [-1] for shape [1] is invalid. When [--dynamic_batch_size] is included, only batch size N can be –1 in [--input_shape].”

## 问题根因
当使用--dynamic_batch_size参数时，ATC工具仅允许输入shape的第一个维度（即Batch维度N）设置为-1，其他维度（如H、W）不能设为-1。原文中input_shape设置为"Placeholder:-1,-1,-1,3"，将H和W也设为-1，违反了该限制。

## 解决方案
修改--input_shape参数，仅将Batch维度（第一个维度）设为-1，其余维度指定具体数值。例如：--input_shape="Placeholder:-1,224,224,3"。

