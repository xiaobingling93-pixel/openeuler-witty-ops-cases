# 使用Paddle模型执行ATC模型转换时报错：E16005: The model has [2] [--domain_version] fields, but only one is allowed

## 内核版本


## 问题现象
由Paddle转换为ONNX的模型文件，在使用ATC工具进行模型转换时，报错：E16005: The model has [2] [--domain_version] fields, but only one is allowed。

## 问题根因
模型中包含两个opset_import（算子集版本）字段，而ATC工具仅允许存在一个--domain_version（即opset_import）字段。

## 解决方案
使用ONNX Python API加载模型后，删除多余的opset_import条目。示例代码如下：
import onnx
original_model = onnx.load("./lpcnet.onnx")
del original_model.opset_import[1]
onnx.save(original_model, './test.onnx')

