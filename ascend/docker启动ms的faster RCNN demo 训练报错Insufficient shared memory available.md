# docker启动ms的faster RCNN demo 训练报错Insufficient shared memory available

## 内核版本


## 问题现象
在使用Docker启动MindSpore的Faster R-CNN demo进行训练时，报错提示“Insufficient shared memory available”（共享内存不足）。

## 问题根因
可能的原因包括：batch_size设置过大；set_prefetch_size()接口参数设置过大；宿主机侧共享内存（shared memory）不足。

## 解决方案
在使用docker run命令创建容器时，添加--ipc=host参数以共享宿主机的内存，或通过--shm-size参数显式指定更大的共享内存大小（例如--shm-size 800g）。

