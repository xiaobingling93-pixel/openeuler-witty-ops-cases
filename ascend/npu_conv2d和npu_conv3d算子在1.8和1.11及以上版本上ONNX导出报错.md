# npu_conv2d和npu_conv3d算子在1.8和1.11及以上版本上ONNX导出报错

## 内核版本


## 问题现象
npu_conv2d和npu_conv3d算子在PyTorch 1.8、1.11及以上版本上导出ONNX模型时，出现报错信息：“_convolution() missing 1 required positional argument: 'allow_tf32'”。

## 问题根因
该问题是由于PyTorch框架的bug导致，在ONNX导出过程中，_convolution函数缺少allow_tf32参数。

## 解决方案
修改torch/onnx/symbolic_opset9.py文件，在第1293行的_convolution函数定义中添加默认参数allow_tf32=None。具体修改为：def _convolution(g, input, weight, bias, stride, padding, dilation, transposed, output_padding, groups, benchmark, deterministic, cudnn_enabled, allow_tf32=None): 可参考PyTorch官方issue #75098和PR #75099。

