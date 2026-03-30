# Vector比对报错：ModuleNotFoundError: No module named 'google'

## 内核版本


## 问题现象
执行Vector比对时，界面弹出报错窗口，提示“未安装protobuf”，并在output栏打印错误信息：ModuleNotFoundError: No module named 'google'，具体发生在导入DumpData_pb2.py模块时。

## 问题根因
操作系统未安装protobuf库，导致无法解析Caffe模型的dump数据，从而在执行Vector比对时因缺少google.protobuf相关模块而报错。

## 解决方案
使用MindStudio安装用户登录服务器，执行命令 pip3.7.5 install protobuf --user 安装protobuf库，然后再进行精度比对。

