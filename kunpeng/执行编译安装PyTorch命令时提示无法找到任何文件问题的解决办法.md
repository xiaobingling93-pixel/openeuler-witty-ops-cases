# 执行编译安装PyTorch命令时提示无法找到任何文件问题的解决办法

## 内核版本


## 问题现象
执行编译安装PyTorch命令 python3 setup.py install 时提示在“/path/to/pytorch/third_party/ios-cmake”目录中无法找到任何CMakeLists.txt、Makefile、setup.py、LICENSE、LICENSE.md、LICENSE.txt文件，错误信息为：Could not find any of CMakeLists.txt,Makefile,setup.py,LICENSE,LICENSE.md,LICENSE.txt in /path/to/pytorch/third_party/ios-cmake。Did you run 'git submodule update --init --recursive'?

## 问题根因
子仓依赖下载失败，导致 third_party/ios-cmake 目录下缺少必要的文件。

## 解决方案
1. 进入 PyTorch 源码目录：cd /path/to/pytorch；2. 删除下载失败的子仓文件夹：rm -rf /path/to/pytorch/third_party/ios-cmake；3. 重新执行获取子仓命令：git submodule update --init --recursive。

