# 编译报错下载apr-1.6.3失败

## 内核版本


## 问题现象
在编译过程中下载apr-1.6.3失败。

## 问题根因


## 解决方案
1. 打开“pom.xml”文件；2. 注释掉文件中两处下载apr-1.6.3的部分（URL分别为http://archive.apache.org/dist/apr/${aprArchiveFile}和http://archive.apache.org/dist/apr/${aprTarGzFile}）；3. 保存并退出编辑；4. 手动下载apr-1.6.3：wget https://archive.apache.org/dist/apr/apr-1.6.3.tar.gz，并将其移动到netty-tcnative-netty-tcnative-parent-2.0.7.Final/openssl-static/target目录；5. 重新执行编译。

