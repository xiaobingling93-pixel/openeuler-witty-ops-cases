# 获取PyTorch源码失败的解决办法

## 内核版本


## 问题现象
获取PyTorch源码时提示unexpected disconnect while reading sideband packet，具体错误包括：error: RPC failed; curl 18 transfer closed with outstanding read data remaining，fatal: early EOF，fatal: fetch-pack: invalid index-pack output。

## 问题根因
网络质量不佳导致代码下载失败。

## 解决方案
重新执行获取源码命令：git clone -b v2.1.2 https://github.com/pytorch/pytorch.git --depth 1

