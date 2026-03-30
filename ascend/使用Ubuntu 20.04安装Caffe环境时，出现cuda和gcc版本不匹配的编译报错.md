# 使用Ubuntu 20.04安装Caffe环境时，出现cuda和gcc版本不匹配的编译报错

## 内核版本


## 问题现象
使用Ubuntu 20.04安装Caffe环境时，编译过程中出现cuda和gcc版本不匹配的错误。

## 问题根因
Ubuntu 20.04默认gcc版本为gcc9，而CUDA 10.0仅支持gcc7，因此在使用默认gcc版本编译时会报错，提示不支持gcc7以上的版本。

## 解决方案
安装gcc7，并将其软链接到CUDA安装目录下的bin目录中，以确保CUDA编译时使用兼容的gcc版本。具体命令如下：sudo apt-get install g++-7 -y；sudo ln -s /usr/bin/gcc-7 /usr/local/cuda-10.0/bin/gcc；sudo ln -s /usr/bin/g++-7 /usr/local/cuda-10.0/bin/g++（路径请根据实际CUDA安装位置调整）。

