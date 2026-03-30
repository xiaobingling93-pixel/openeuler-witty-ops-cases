# ATC模型转换时ONNX文件Opset版本不兼容，报错“E19010”

## 内核版本


## 问题现象
用户使用ATC工具将ONNX模型转换成适配OrangePi Alpro的OM模型时，报错提示“ATC run failed, Please check the detail log, Try 'atc --help' for more information.”，错误码为“E19010”。具体日志显示：“E19010: No parser is registered for Op [model1 div node, optype [ai.onnx::23::Div]]。”

## 问题根因
ATC工具中无对应算子的解析器，原因是当前ONNX模型使用的Opset版本为v23，而Div算子在当前CANN版本中仅支持Opset v8至v18，v23超出了支持范围。

## 解决方案
将ONNX模型的Opset版本降级至官方文档中Div算子所支持的版本范围（如v18或更低），再重新进行ATC模型转换。

