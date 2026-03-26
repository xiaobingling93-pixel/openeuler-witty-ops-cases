# ATC转换OM失败，报错信息：E19999 Param:src_out_anchor_is nullpt

## 内核版本


## 问题现象
使用ATC工具将模型转换为OM格式时失败，报错信息为“E19999 Param:src_out_anchor_is nullpt”。通过日志分析发现，问题出现在Resize_1算子，其输入为空，导致无法完成模型转换。

## 问题根因
Resize算子的input信息缺失（为空），在ATC转换过程中无法正确处理该算子，从而引发空指针错误。

## 解决方案
补全Resize算子的input信息。可通过auto_optimizer工具加载ONNX模型，添加空的initializer，并为Resize算子的inputs[1]和inputs[2]赋值，然后保存修改后的模型用于后续转换。

