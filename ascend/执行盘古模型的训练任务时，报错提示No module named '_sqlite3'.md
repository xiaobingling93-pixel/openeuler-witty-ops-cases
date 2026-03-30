# 执行盘古模型的训练任务时，报错提示No module named '_sqlite3'

## 内核版本


## 问题现象
执行盘古模型的训练任务时，报错提示No module named '_sqlite3'。

## 问题根因
环境中缺少盘古镜像需要的sqlite3依赖，导致训练任务失败。

## 解决方案
1. 根据当前的操作系统类型，安装sqlite3依赖：Ubuntu系统执行'sudo apt-get install libsqlite3-dev'，CentOS系统执行'sudo yum install sqlite-devel'。2. 重新编译Python（以Python 3.7为例）：下载Python-3.7.5.tar.xz软件包，解压后执行'./configure --prefix=/usr/local/python3.7.5 --enable-shared'，然后执行'make && make install'完成安装。

