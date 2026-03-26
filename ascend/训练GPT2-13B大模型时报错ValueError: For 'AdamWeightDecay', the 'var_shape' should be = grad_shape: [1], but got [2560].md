# 训练GPT2-13B大模型时报错ValueError: For 'AdamWeightDecay', the 'var_shape' should be = grad_shape: [1], but got [2560]

## 内核版本


## 问题现象
在使用MindSpore 1.9.0训练GPT2-13B大模型时，出现错误：ValueError: For 'AdamWeightDecay', the 'var_shape' should be = grad_shape: [1], but got [2560]。

## 问题根因
AdamWeightDecay优化器在进行切分（optimizer_shard=True）时存在不兼容或bug，导致变量形状（var_shape）与梯度形状（grad_shape）不一致。

## 解决方案
临时解决方案是将配置文件run_gpt2_13b.yaml中的optimizer_shard设置为False，但这会增加内存消耗；推荐使用MindSpore 1.9.1或更高版本，并保持optimizer_shard为True以正确支持优化器切分。

