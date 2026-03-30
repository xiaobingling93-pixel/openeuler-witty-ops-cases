# 20节点160卡跑baichuan-7B模型报错out of memory，但2节点16卡能跑通

## 内核版本


## 问题现象
在20节点160卡环境下运行baichuan-7B模型时出现out of memory错误，其中dp/mp/pp设置为40/1/4；而在2节点16卡环境下（dp/mp/pp设置为8/1/2）可以正常运行。

## 问题根因
parallel_config中optimizer_shard未生效，原因是hidden_size（4096）不能被数据并行度dp（40）整除，导致优化器切分未开启；同时MindSpore版本对optimizer_shard的支持存在问题。

## 解决方案
调整数据并行度dp为能整除hidden_size（4096）的值（例如32），或者通过context.set_auto_parallel_context(optimizer_weight_shard_size=8)显式设置优化器权重切分大小，确保其可被整除，从而启用优化器切分以降低显存占用。

