# 数据预处理中存在tf.Variable导致训练异常

## 内核版本


## 问题现象
TensorFlow网络执行时，报错：tensorflow.python.framework.errors_impl.FailedPreconditionError: Error while reading resource variable inference/embed_continuous from Container: localhost. This could mean that the variable was uninitialized. Not found: Resource localhost/inference/embed_continuous/N10tensorflow3VarE does not exist.

## 问题根因
数据预处理脚本中使用了tf.Variable变量。在昇腾平台上运行时，tf.Variable变量的执行在Host侧，而其初始化在Device侧，导致变量执行与初始化不在同一设备上，从而引发训练异常。

## 解决方案
修改训练脚本，将tf.Variable替换为常量。例如，将 batch_size = tf.Variable(tf.placeholder(tf.int64, [], 'batch_size'), trainable=False, collections=[]) 改为 batch_size = 64，并直接用于 train_dataset.batch(batch_size, drop_remainder=True)。

