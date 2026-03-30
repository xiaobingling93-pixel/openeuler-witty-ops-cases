# MindSpore报RuntimeErrorReduceSum算子不支持8维及以上的输入而报错

## 内核版本


## 问题现象
在使用MindSpore 1.6.0版本进行模型训练时，构建了一个包含10维输入张量的ReduceSum单算子网络，执行时报错：RuntimeError: In op, the num of dimensions of input/output[x] should be in the range of [0, 8], but actually is [10]。

## 问题根因
ReduceSum算子在当前版本中仅支持输入张量维度在[0, 8]范围内，而用户代码中传入的张量维度为10，超出了算子支持的最大维度限制。

## 解决方案
将输入张量的维度修改为不超过8维，例如将原10维张量np.random.randn(10, 5, 4, 4, 4, 4, 4, 4, 4, 4)改为8维张量np.random.randn(10, 5, 4, 4, 4, 4, 4, 4)，即可正常运行并输出结果。

