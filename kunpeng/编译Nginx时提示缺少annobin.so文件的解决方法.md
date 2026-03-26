# 编译Nginx时提示缺少annobin.so文件的解决方法

## 内核版本


## 问题现象
在编译安装Nginx 1.14.2时，提示“Inaccessible plugin file /usr/local/lib/gcc/aarch64-unknown-linux-gnu/8.5.0/plugin/annobin.so”。

## 问题根因
缺少annobin.so文件。

## 解决方案
1. 使用Yum源安装annobin：yum install -y annobin；
2. 设置软链接：cd /usr/local/lib/gcc/aarch64-unknown-linux-gnu/8.5.0/plugin，然后执行 ln -sf /usr/lib/gcc/aarch64-redhat-linux/8/plugin/annobin.so.0.0.0 annobin.so.0 和 ln -sf /usr/lib/gcc/aarch64-redhat-linux/8/plugin/annobin.so.0.0.0 annobin.so；
3. 重新编译Nginx：进入nginx源码目录，执行 make clean，然后运行 ./configure 配置命令，再执行 make -j60 和 make install。

