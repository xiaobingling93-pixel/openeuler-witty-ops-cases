# msame推理ssd-resnet34报模型加载失败

## 内核版本


## 问题现象
在CANN 6.0.1或6.3环境下，使用msame工具对ssd-resnet34模型进行推理时，报错“load model from file failed”，提示无法加载指定路径下的.om模型文件。该路径下其他.om模型可正常加载，说明路径无误。

## 问题根因
原始pb模型中包含TensorFlow V1版本的控制流算子（如Enter、Merge、Switch等），而昇腾GE Runtime 2.0不支持V1控制流算子，导致模型转换或加载失败。

## 解决方案
使用提供的工具链（xlacompile、summarize_graph和gen_gdl.sh）将原始pb模型中的V1控制流算子转换为V2版本：首先用summarize_graph获取输出节点名，然后修改gen_gdl.sh脚本中的模型路径和输出节点，执行脚本生成V2版本的pb模型，最后使用ATC工具将V2 pb模型重新转换为.om格式用于推理。

