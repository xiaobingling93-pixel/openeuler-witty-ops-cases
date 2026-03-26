# 数据预处理使用tf.keras.backend.zero生成变量，训练报错变量未初始化

## 内核版本


## 问题现象
训练过程中报错变量算子未初始化。

## 问题根因
数据预处理使用tf.keras.backend.zero生成变量，导致变量算子无法下沉到Device侧执行，从而引发变量算子初始化失败。

## 解决方案
修改训练脚本，不使用tf.keras.backend.zero生成变量，而直接使用TensorFlow原生接口tf.zeros以tensor形式在Host侧生成变量。例如，将'y = {‘mlm_loss’: tf.keras.backend.zero([1]), ‘mlm_acc’: tf.keras.backend.zero([1])}'修改为'y = {‘mlm_loss’: tf.zeros([1]), ‘mlm_acc’: tf.zeros([1])}'。

