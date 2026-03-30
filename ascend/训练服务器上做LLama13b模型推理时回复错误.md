# 训练服务器上做LLama13b模型推理时回复错误

## 内核版本


## 问题现象
在Atlas800 9000 A2训练服务器上，利用Mindformers套件进行Llama13B模型推理时，推理结果不正确。

## 问题根因
推理精度配置不正确。

## 解决方案
在推理启动脚本中调用set_context时，设置precision_mode参数以确保正确的推理精度。具体配置方法参考MindSpore官方文档：https://www.mindspore.cn/docs/zh-CN/r2.1/api_python/mindspore/mindspore.set_context.html?highlight=precision_mode。

