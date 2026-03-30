# 查看zlib库加速引擎是否生效时提示部分库找不到的解决办法

## 内核版本


## 问题现象
源码安装KAE后，通过执行命令 ldd /usr/local/kaezip/lib/libz.so.1.2.11 查看zlib加速库是否链接到动态库时，提示 libkaezip.so、libwd.so.2 等库 not found 的错误信息。

## 问题根因


## 解决方案
1. 编辑 /etc/ld.so.conf 文件；2. 在文件末尾添加路径：/usr/local/lib 和 /usr/local/kaezip/lib；3. 执行 ldconfig 命令使配置生效。之后重新执行 ldd 命令即可正常显示链接的动态库。

