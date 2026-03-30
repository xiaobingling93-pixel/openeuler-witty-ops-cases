# 编译报错libressl-2.5.5下载失败

## 内核版本


## 问题现象
编译时提示libressl-2.5.5下载失败。

## 问题根因


## 解决方案
1. 将下载的apr-1.6.3软件包放置于netty-tcnative-netty-tcnative-parent-2.0.7.Final/libressl-static/target目录下。2. 修改libressl-static/pom.xml文件，注释掉其中下载libressl-2.5.5的代码行（src="http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/${libresslArchive}" ...）。3. 手动下载libressl-2.5.5：wget http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.5.5.tar.gz，并将其移至netty-tcnative-netty-tcnative-parent-2.0.7.Final/libressl-static/target目录。4. 执行mvn install继续编译打包到Maven本地仓库。

