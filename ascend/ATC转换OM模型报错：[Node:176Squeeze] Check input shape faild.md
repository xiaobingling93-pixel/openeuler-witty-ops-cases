# ATC转换OM模型报错：[Node:176Squeeze] Check input shape faild

## 内核版本


## 问题现象
Mindspore训练的flyspeech模型导出ONNX文件后，使用ATC工具转OM模型时报错：[Node:176Squeeze] Check input shape faild。

## 问题根因
Squeeze算子要求指定压缩的维度大小必须为1，但实际输入shape为[1,512,8,193]，其中dim[2]=8≠1，导致输入shape不匹配，从而引发转换失败。

## 解决方案
当前支持导出ONNX的模型清单中不包含该模型，无法保证ONNX文件的正确性，建议改用导出air格式的文件，并重新执行ATC命令进行模型转换。

