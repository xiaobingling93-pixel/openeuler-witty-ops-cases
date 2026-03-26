# 安装OpenSSL时提示No such file or directory的解决方法

## 内核版本


## 问题现象
确认OpenSSL是否安装成功时，提示“openssl: error while loading shared libraries: libcrypto.so.1.1: cannot open shared object file: No such file or directory”。

## 问题根因
OpenSSL缺少libcrypto.so.1.1库文件。

## 解决方案
1. 执行以下命令，设置软链接：
   ln -s /usr/local/lib/libssl.so.1.1 /usr/lib64/libssl.so.1.1
   ln -s /usr/local/lib/libcrypto.so.1.1 /usr/lib64/libcrypto.so.1.1
   ldconfig
2. 再次确认OpenSSL是否安装成功，执行 openssl version 查看版本信息。

