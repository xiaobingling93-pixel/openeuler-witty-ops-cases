# 仅在某个Device上保存Checkpoint数据

## 内核版本


## 问题现象
在分布式训练场景下，用户希望只在某个Device（如rank 0）上保存checkpoint数据，而不希望在其他Device上保存。

## 问题根因
原始TensorFlow代码中使用Horovod的hvd.rank()判断是否为主设备来控制checkpoint保存，但在昇腾NPU环境下需使用适配的NPUEstimator和get_rank_id()函数，并且在非主设备上应将save_checkpoints_steps设为0而非None。

## 解决方案
修改训练脚本，使用NPUEstimator替代tf.estimator.Estimator，并在NPURunConfig中设置save_checkpoints_steps=50 if get_rank_id() == 0 else 0，确保仅在指定Device上保存checkpoint。

