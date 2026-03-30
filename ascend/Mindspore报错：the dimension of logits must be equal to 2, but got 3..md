# Mindspore报错：the dimension of logits must be equal to 2, but got 3.

## 内核版本


## 问题现象
在使用MindSpore 1.6.0进行模型训练时，调用SoftmaxCrossEntropyWithLogits算子传入了三维的logits张量（shape为[1,2,5]），导致报错：'the dimension of logits must be equal to 2, but got 3'。

## 问题根因
SoftmaxCrossEntropyWithLogits算子要求输入的logits必须是二维张量（shape为(N, C)），但用户传入的是三维张量，不符合算子接口的维度要求。

## 解决方案
在调用SoftmaxCrossEntropyWithLogits前，先将三维的logits和labels通过reshape操作转换为二维（如(L*N, C)），计算损失后再将输出reshape回期望的形状（如(N, 1)）。

