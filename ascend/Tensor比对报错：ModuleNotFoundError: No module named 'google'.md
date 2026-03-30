# Tensor比对报错：ModuleNotFoundError: No module named 'google'

## 内核版本


## 问题现象
执行Vector比对时，界面弹出报错窗口，并在“output”栏打印错误信息：ModuleNotFoundError: No module named 'google'。具体报错发生在尝试导入DumpData_pb2.py时，提示缺少google模块。

## 问题根因
操作系统未安装protobuf库，导致无法解析Caffe模型的dump数据，从而在导入相关protobuf生成文件时失败。

## 解决方案
使用pip3.7.5命令安装protobuf库：pip3.7.5 install protobuf --user，安装完成后重新进行精度比对。

