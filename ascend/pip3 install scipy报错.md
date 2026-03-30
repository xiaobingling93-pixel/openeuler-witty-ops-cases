# pip3 install scipy报错

## 内核版本


## 问题现象
在执行pip3 install scipy命令时，安装失败并提示在/usr/lib64目录下未找到lapack和blas的库。

## 问题根因
系统中虽然存在liblapack.so.3和libblas.so.3库文件，但scipy安装过程无法识别带版本号的so.3库文件，需要对应不带版本号的liblapack.so和libblas.so文件。

## 解决方案
在/usr/lib64目录下为liblapack.so.3和libblas.so.3创建对应的软链接：
ln -s libblas.so.3 libblas.so
ln -s liblapack.so.3 liblapack.so

