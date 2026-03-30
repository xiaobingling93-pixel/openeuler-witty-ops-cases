# 量化过程中提示某层bias量化超出int32范围

## 内核版本


## 问题现象
在模型量化过程中，系统报错提示某层（如FlowNetS/decoding/deconv5_0/conv2d_transpose）的bias量化值超出了int32的表示范围[-2147483648, 2147483647]，具体表现为tensorflow.python.framework.errors_impl.InvalidArgumentError异常，错误信息显示量化后的bias值（如3.35e+12）远大于int32最大值（约2.15e+9）。

## 问题根因
由于权重scale（scale_w）和数据scale（scale_d）取值过小，而原始bias值较大，导致量化后的bias = bias / (scale_w * scale_d) 数值过大，超出了int32类型的可表示范围。

## 解决方案
根据错误提示，将报错中指定的层（例如FlowNetS/decoding/deconv5_0/conv2d_transpose）添加到量化跳过列表（skip layer）中，避免对该层进行量化处理。

