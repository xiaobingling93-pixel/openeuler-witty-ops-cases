# 使用第三方库transformers跑模型推理时，报错“cannot allocate memory in static TLS block”

## 内核版本


## 问题现象
使用第三方库transformers进行模型推理时，系统报错“cannot allocate memory in static TLS block”。

## 问题根因
glibc.so本身的bug。

## 解决方案
执行命令：export LD_PRELOAD=$LD_PRELOAD:/usr/local/python3.10.2/lib/python3.10/site-packages/torch/lib/../../torch.libs/libgomp-6e1a1d1b.so.1.0.0

