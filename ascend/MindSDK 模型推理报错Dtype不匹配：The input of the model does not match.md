# MindSDK 模型推理报错Dtype不匹配：The input of the model does not match

## 内核版本


## 问题现象
MindSDK模型推理时报错“The input of the model does not match”，提示输入数据类型与模型期望的类型不匹配。

## 问题根因
MindSDK图片内容保存的数据类型为int8，而模型转换时未配置AIPP（AI Preprocessing），导致模型仍期望fp32类型的输入，从而引发数据类型不匹配错误。

## 解决方案
在模型转换时添加AIPP配置文件，将输入数据从int8正确预处理为模型所需的fp32格式。具体方法是使用atc工具转换模型时指定--insert_op_conf参数，并提供包含AIPP配置的.aippconfig文件。

