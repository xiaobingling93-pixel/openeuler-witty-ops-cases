# 使用第三方库transformers跑模型训练时，报错“cannot allocate memory in static TLS block”

## 内核版本


## 问题现象
在使用transformers库进行模型训练时，出现错误：ImportError: /usr/local/python3.7.5/lib/python3.7/site-packages/sklearn/__check_build/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block。

## 问题根因
glibc.so本身的bug。

## 解决方案
执行命令：export LD_PRELOAD=$LD_PRELOAD:/usr/local/python3.7.5/lib/python3.7/site-packages/scikit_learn.libs/libgomp-d22c30c5.so.1.0.0

