# 编译ScaNN过程中没有Python.h文件的解决办法

## 内核版本


## 问题现象
执行编译ScaNN命令时提示错误：fatal error: Python.h: No such file or directory，导致编译失败。

## 问题根因
ScaNN编译过程中需要引用Python.h头文件，但由于未安装python3-devel开发包或未设置Python头文件路径，导致编译器无法找到该文件。

## 解决方案
1. 确认是否安装python3-devel开发包，检查路径/usr/include/python3.9/下是否存在Python.h文件；若不存在，执行命令 yum install python3-devel 安装。
2. 将Python头文件路径添加到环境变量中：export C_INCLUDE_PATH=/usr/include/python3.9:$C_INCLUDE_PATH 和 export CPLUS_INCLUDE_PATH=/usr/include/python3.9:$CPLUS_INCLUDE_PATH。
3. 重新执行编译命令：bazel clean; CC=gcc bazel build -c opt --cxxopt="-std=c++17" --copt=-fsized-deallocation --copt=-w --copt=-O3 --cxxopt=-O3 --copt=-march=armv8.2-a+lse+sve+f64mm --cxxopt=-march=armv8.2-a+lse+sve+f64mm --copt=-msve-vector-bits=256 --cxxopt=-msve-vector-bits=256 :build_pip_pkg。

