# 安装toolkit包时，出现找不到grpc依赖库的问题

## 内核版本


## 问题现象
安装toolkit包时报错找不到grpc依赖库，提示Package is not installed on the path /usr/local/Ascend/ascend-toolkit/20.0.0.SPC200/arm64-linux_gcc4.8.5。

## 问题根因
环境中安装了多个版本的Python（如python3.7和python3.7.5），而grpc依赖库仅安装在python3.7.5路径下，导致其他Python版本无法调用该依赖。

## 解决方案
通过创建软链接，将python3.7与python3.7.5指向同一个Python依赖库路径，命令如下：
ln -s /usr/local/python3.7.5/bin/python3 /usr/bin/python3.7.5
ln -s /usr/local/python3.7.5/bin/pip3 /usr/bin/pip3.7.5
ln -s /usr/local/python3.7.5/bin/python3 /usr/bin/python3.7
ln -s /usr/local/python3.7.5/bin/pip3 /usr/bin/pip3.7

