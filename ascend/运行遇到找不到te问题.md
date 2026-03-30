# 运行遇到找不到te问题

## 内核版本


## 问题现象
运行时遇到找不到te模块的问题。

## 问题根因
依赖版本需要更新。

## 解决方案
1. 进入插件目录：开发态路径为 /usr/local/Ascend/ascend-toolkit/latest/{arch}-linux/lib64，用户态路径为 /usr/local/Ascend/nnae/latest/{arch}-linux/lib64；2. 手动更新依赖：执行 pip3 install --upgrade te-0.4.0-py3-none-any.whl。

