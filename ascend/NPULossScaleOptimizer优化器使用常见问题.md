# NPULossScaleOptimizer优化器使用常见问题

## 内核版本


## 问题现象
使用NPULossScaleOptimizer优化器时，如果训练脚本中在tf.control_dependencies上下文内创建优化器并调用minimize方法，会出现'Placeholder not support'报错。

## 问题根因
动态loss_scale_manager中包含变量，若在tf.control_dependencies上下文内创建loss_scale_manager，会导致Variable初始化时执行出错。

## 解决方案
应在tf.control_dependencies上下文之外先创建loss_scale_manager，再在上下文内使用NPULossScaleOptimizer。例如：loss_scale_manager = ExponentialUpdateLossScaleManager(init_loss_scale=2**32, incr_every_n_steps=1000, decr_every_n_nan_or_inf=2, decr_ratio=0.5)；然后在with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS))内调用NPULossScaleOptimizer(...).minimize(loss)。

