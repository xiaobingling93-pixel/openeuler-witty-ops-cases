# 指定ONNX输出节点转成OM后，用ATC工具转OM时报错误码E19999

## 内核版本


## 问题现象
使用ATC工具将ONNX模型转换为OM模型时，指定输出节点后报错：E19999 User specified tensor[p2o.Concat.38] is not output of graph.

## 问题根因
指定的输出节点名称不正确或该节点在图中不存在；实际应指定为节点名加输出索引的形式（如p2o.Concat.38:0），且节点名必须是原始ONNX模型中的有效节点。

## 解决方案
1. 使用Netron等工具打开ONNX模型，确认节点p2o.Concat.38确实存在；2. 在ATC转换命令中正确指定输出节点为p2o.Concat.38:0，并确保节点名使用双引号包裹，多个节点用英文分号分隔。

