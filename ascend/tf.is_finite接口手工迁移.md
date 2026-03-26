# tf.is_finite接口手工迁移

## 内核版本


## 问题现象
CANN不支持tf.is_finite接口，导致用户在使用TensorFlow进行模型训练时无法直接调用该接口判断梯度是否溢出。

## 问题根因
CANN框架本身未实现对TensorFlow中tf.is_finite接口的支持，因此需要用户在迁移脚本时手动调整相关逻辑。

## 解决方案
将梯度是否溢出的判断逻辑交由NPULossScaleOptimizer处理，移除用户脚本中显式使用tf.is_finite的代码。具体做法是删除all_are_finite的计算以及基于该条件的global_step更新逻辑，并确保优化器被NPULossScaleOptimizer包装，从而自动处理梯度溢出问题。

