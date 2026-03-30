# 使用NPU Loss Scale优化器后，训练不收敛

## 内核版本


## 问题现象
word2vec网络在关闭NPU Loss Scale时训练收敛，但启用NPU Loss Scale优化器后训练不收敛。

## 问题根因
混合精度模式下，Log算子使用了NZ格式，导致输入数据被Transdata操作补0，而Log算子对0取对数会产生无穷大（溢出）。由于这些0并非原始有效数据，而是格式转换引入的填充值，因此持续触发溢出检测，使动态Loss Scale不断衰减至0，最终导致训练无法收敛。

## 解决方案
使用静态Loss Scale并关闭溢出检查（设置enable_overflow_check=False），因为该网络中的溢出由非有效数据引起，不影响最终梯度结果，关闭检查后可保证训练收敛。

