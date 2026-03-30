# Vision SDK报错： _StreamManagerApi.so: undefined symbol: PyCMethod_New

## 内核版本


## 问题现象
执行 python import StreamManagerApi 命令时，提示报错信息：_StreamManagerApi.so: undefined symbol: PyCMethod_New。

## 问题根因
Python版本不是3.9，而Vision SDK要求必须使用Python 3.9版本。

## 解决方案
切换Python版本至3.9。

