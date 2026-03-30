# 模型转换失败，日志中有“input x shape is empty”的内容信息

## 内核版本


## 问题现象
模型转换失败，日志中出现“input x shape is empty”的错误信息。

## 问题根因
原始的TensorFlow模型输入是动态shape（如“?×299×299×3”），在转换模型时未指定input_shape参数，导致转换工具无法确定输入张量的具体形状，从而报错。

## 解决方案
1. 使用Netron工具查看模型，确认模型输入的shape；2. 对于动态shape的模型，在使用ATC工具进行模型转换时必须显式指定input_shape参数，例如：atc --model=./resnetv2.pb --framework=3 --input_shape="input_tensor:8,299,299,3" --input_format="NHWC" --output=./resnetv2 --soc_version=Ascend310。

