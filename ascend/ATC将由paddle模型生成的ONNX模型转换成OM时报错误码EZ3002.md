# ATC将由paddle模型生成的ONNX模型转换成OM时报错误码EZ3002

## 内核版本


## 问题现象
ATC工具将由paddle模型生成的ONNX模型转换成OM时，Cast和GatherV2算子报EZ3002错误码。

## 问题根因
Cast和GatherV2算子在当前CANN版本中不支持动态shape的场景。

## 解决方案
确认模型输入是否是动态shape；如果是，则重新安装CANN 6.3.RC2版本的安装包。

