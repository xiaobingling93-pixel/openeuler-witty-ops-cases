# 安装openssl-devel时提示so文件冲突

## 内核版本


## 问题现象
运行yum install -y openssl-devel命令进行安装时，出现so文件冲突错误。

## 问题根因
原生包 openssl-libs-1.1.1f-7.h1.eulerosv2r9 和即将安装的 openssl-SMx-libs-1.1.1f-7.eulerosv2r9 包冲突。

## 解决方案
下载openssl的rpm包，使用rpm命令强制安装：1. 创建并进入新文件夹；2. 使用yum install --downloadonly --downloaddir=. openssl-devel下载rpm包；3. 执行rpm -Uvh *.rpm --force强制安装。

