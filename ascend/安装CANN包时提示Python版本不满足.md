# 安装CANN包时提示Python版本不满足

## 内核版本


## 问题现象
CANN软件包安装时提示错误：[ERROR] There is no python3.7,python3.8,python3.9,python3.10,python3.11 in the current environment。

## 问题根因
CANN版本要求Python版本在3.7.x至3.11.4之间，但当前环境中实际使用的Python版本不符合该要求，可能是因为系统中存在多个Python版本，且默认使用的版本不在支持范围内。

## 解决方案
1. 使用命令 python3 --version、ldd $(which python3) 和 pip3 --version 检查当前Python版本及路径；2. 若版本不符，通过设置环境变量指定符合要求的Python路径（例如 export LD_LIBRARY_PATH=/usr/local/python3.7.5/lib:$LD_LIBRARY_PATH 和 export PATH=/usr/local/python3.7.5/bin:$PATH）；3. 若仍存在问题，卸载当前Python并参考官方文档重新编译安装合适版本。

