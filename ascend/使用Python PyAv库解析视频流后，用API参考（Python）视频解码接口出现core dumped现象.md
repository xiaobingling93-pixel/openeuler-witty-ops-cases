# 使用Python PyAv库解析视频流后，用API参考（Python）视频解码接口出现core dumped现象

## 内核版本


## 问题现象
使用Python PyAv库解析视频流后，调用Python视频解码接口对视频帧进行解码时出现Segmentation fault (core dumped)现象。

## 问题根因
PyAv库的版本过高。

## 解决方案
安装10.0.0或以下版本的PyAv库。以10.0.0版本为例，安装命令如下：pip3 install av==10.0.0

