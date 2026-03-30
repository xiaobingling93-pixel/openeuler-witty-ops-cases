# 在模型运行时遇到告警“current tensor is running as_strided, don't perform inplace operations on the returned value.”

## 内核版本


## 问题现象
在模型运行时出现告警："current tensor is running as_strided, don't perform inplace operations on the returned value."，具体表现为对as_strided操作返回的tensor执行了inplace赋值（如b[:, :, :, :, 0] = tmp3），并可能伴随精度问题。

## 问题根因
在Ascend Extension for PyTorch中，某些私有格式（internal format）不支持as_strided操作。当卷积类算子（如conv1d、conv2d、conv3d、_convolution等）输出私有格式的tensor后，若对其进行as_strided操作，再执行inplace修改，会触发该告警。这是因为私有格式经过as_strided后不再支持inplace操作。

## 解决方案
若出现该告警且存在精度问题，可通过设置 torch.npu.config.allow_internal_format = False 来关闭私有格式。此设置将使所有算子不再生成私有格式的tensor，从而避免该问题，但可能对性能产生一定影响。

