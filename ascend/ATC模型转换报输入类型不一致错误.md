# ATC模型转换报输入类型不一致错误

## 内核版本


## 问题现象
ATC模型转换过程中报错：dtype of inputs must be same。

## 问题根因
concat算子的输入类型必须保持一致，但模型中存在float32和float16两种不同类型的输入。

## 解决方案
在netron中打开模型，定位concat算子的输入，在float16输入后添加Cast算子将其转换为float32。具体方法是在ONNX模型中通过代码插入Cast节点，例如：ew_cast = g.add_node('new_cast', 'Cast', attrs={'to':1})，然后使用g.insert_node('Gather_66', new_cast)在指定位置插入该算子。

