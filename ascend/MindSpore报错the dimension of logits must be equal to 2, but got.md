# MindSpore报错the dimension of logits must be equal to 2, but got

## 内核版本


## 问题现象
在使用MindSpore的SoftmaxCrossEntropyWithLogits算子时，传入的logits张量维度为3维，导致报错：'the dimension of logits must be equal to 2, but got 3'。具体输入数据为shape [[[2, 4, 1, 4, 5], [2, 1, 2, 4, 3]]]，即形状为(1, 2, 5)。

## 问题根因
SoftmaxCrossEntropyWithLogits算子要求输入logits的维度必须为2维（形状为(N, C)），但实际传入的是3维张量，不符合API接口的输入要求。

## 解决方案
在调用SoftmaxCrossEntropyWithLogits前，先将3维的logits和labels通过reshape转换为2维（L*N, C），计算loss后再将输出reshape回期望的形状（如(N, 1)）。例如：logits, labels = logits.reshape(L*N, C), labels.reshape(L*N, C)，计算后out = out.reshape(N, 1)。

