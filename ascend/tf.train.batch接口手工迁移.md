# tf.train.batch接口手工迁移

## 内核版本


## 问题现象
TensorFlow不建议使用tf.train.batch接口通过队列形式处理输入数据。

## 问题根因
TensorFlow官方已不推荐使用基于队列的tf.train.batch接口处理输入数据，建议改用tf.data.Dataset API；若仍需在CANN上使用该接口，则需将num_threads参数设为1以避免兼容性问题。

## 解决方案
将tf.train.batch调用中的num_threads参数从大于1的值（如2）修改为1。例如，原始脚本中num_threads=2，迁移后应设置为num_threads=1，其余参数保持不变。

