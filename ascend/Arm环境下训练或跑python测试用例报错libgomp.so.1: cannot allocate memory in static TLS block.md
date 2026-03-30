# Arm环境下训练或跑python测试用例报错libgomp.so.1: cannot allocate memory in static TLS block

## 内核版本


## 问题现象
在Arm环境下训练模型或者运行Rec SDK的Python测试用例时，出现错误提示：libgomp.so.1: cannot allocate memory in static TLS block。

## 问题根因
libgomp.so.1未被正确加载，导致程序无法分配静态TLS（Thread Local Storage）内存块。

## 解决方案
在运行脚本中添加环境变量：export LD_PRELOAD=/usr/local/gcc7.3.0/lib64/libgomp.so.1，以强制预加载指定路径下的libgomp.so.1库。

