# 青松服务器Kylin V10 sp1操作系统，源码方式安装完Python-3.9.2后，pip3工具无法使用

## 内核版本


## 问题现象
在青松服务器Kylin V10 sp1操作系统上通过源码方式安装Python-3.9.2后，使用pip3时出现警告："WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available."，导致pip3无法正常使用。

## 问题根因
系统自带的openssl版本过低，无法满足pip对TLS/SSL模块的需求，导致Python在编译时未能正确启用ssl模块。

## 解决方案
手动升级openssl版本：1. 从openssl官网下载openssl-1.1.1m.tar.gz源码包；2. 上传至服务器并解压；3. 执行编译安装（./config --prefix=/usr/local/openssl no-zlib && make -j32 && make install）；4. 备份原有openssl文件；5. 创建新的软链接以更新openssl路径，包括头文件、库文件和可执行文件。

