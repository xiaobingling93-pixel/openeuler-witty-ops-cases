# 镜像内使用CANN及上层应用libmindspore_ascend.so failed

## 内核版本


## 问题现象
安装后使用CANN及上层应用时，libmindspore_ascend.so加载失败，且无法通过LD_LIBRARY_PATH添加so库。

## 问题根因
在物理机未安装toolbox的情况下，启动容器时未正确挂载Ascend设备和驱动目录，导致容器内缺少必要的设备文件和驱动支持。

## 解决方案
使用docker run命令启动容器时，显式挂载Ascend相关设备（如/dev/davinci0、/dev/davinci_manager等）以及驱动目录（/usr/local/Ascend/driver）和npu-smi工具，确保容器内具备运行CANN及上层应用所需的环境。

