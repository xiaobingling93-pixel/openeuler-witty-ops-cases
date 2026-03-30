# 编译安装时显示无法访问boringssl的下载链接的解决方法

## 内核版本


## 问题现象
编译安装时显示无法访问BoringSSL的下载链接，提示“unable to access 'https://boringssl.googlesource.com/boring/'”。

## 问题根因
boringssl-static模块编译时会拉取boringssl项目的源码，源码中默认的下载地址为https://boringssl.googlesource.com/boringssl。如果编译环境不能访问默认的BoringSSL资源，则需要修改下载地址。

## 解决方案
1. 在源码的“boringssl-static”路径下，打开pom.xml文件：vim /home/netty-tcnative-netty-tcnative-parent-2.0.28.Final/boringssl-static/pom.xml
2. 按“i”进入编辑模式，将第82行的下载地址修改为：https://github.com/google/boringssl
3. 按“Esc”键，输入:wq!，按“Enter”保存并退出编辑。
4. 重新执行编译命令：mvn clean install

