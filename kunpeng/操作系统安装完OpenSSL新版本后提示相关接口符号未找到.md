# 操作系统安装完OpenSSL新版本后提示相关接口符号未找到

## 内核版本


## 问题现象
执行rpm命令或系统OpenSSL命令时出现类似“symbol EVP_md2 version OPENSSL_1_1_0 not defined in file libcrypto.so.1.1 with link time reference”的重定位错误。

## 问题根因
当OpenSSL动态库路径被设置在LD_LIBRARY_PATH环境变量中，或安装在/usr/local/lib目录下（且该路径已配置在/etc/ld.so.conf中）时，系统工具调用OpenSSL动态库会优先加载系统原有版本而非用户新安装的版本，导致符号版本不匹配和链接冲突。

## 解决方案
推荐按照《鲲鹏加速引擎 用户指南》中的“安装OpenSSL/Tongsuo”章节正确安装OpenSSL，并参考“软件安装”章节安装KAE加速引擎。若需将/usr/local/lib加入库搜索路径，应通过指定前缀和运行时库路径编译安装OpenSSL：执行“./config --prefix=/usr/local/openssl -Wl,-rpath,/usr/local/openssl/lib && make && make install”。对于RPM方式安装的KAE加速器，使用“rpm -ivh libkae-1.0.1-1.euler2.0.aarch64.rpm --prefix=/usr/local/openssl/lib/engines-1.1”；对于源码安装，则执行“cd KAE && chmod +x configure && ./configure --openssl_path=/usr/local/openssl && make clean && make && make install”。

