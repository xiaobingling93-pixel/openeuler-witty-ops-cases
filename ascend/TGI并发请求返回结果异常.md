# TGI并发请求返回结果异常

## 内核版本


## 问题现象
llama-13b部署TGI推理框架后，跑8个串行请求时返回结果正常，但跑8个并行请求时返回结果异常。

## 问题根因
config文件中的model_type取值为xverse，而开发时未适配该类型。

## 解决方案
将config文件中的model_type取值改为llama。

