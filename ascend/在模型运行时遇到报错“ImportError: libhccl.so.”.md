# 在模型运行时遇到报错“ImportError: libhccl.so.”

## 内核版本


## 问题现象
在模型运行时出现错误：ImportError: libhccl.so: cannot open shared object file: No such file or directory。

## 问题根因
缺少HCCL库文件。当前使用的PyTorch安装包默认启用了NPU和HCCL功能，但在运行时未将HCCL模块路径添加到环境变量中，导致系统无法找到libhccl.so共享库文件。

## 解决方案
执行命令：source Ascend-cann-toolkit安装目录/Ascend-toolkit/set_env.sh，以设置包含HCCL库的环境变量。

