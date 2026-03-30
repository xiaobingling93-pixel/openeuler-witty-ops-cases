# CentOS 7.6到openEuler 20.03-LTS版本的二进制文件迁移

## 内核版本


## 问题现象
将软件从CentOS 7.6迁移到openEuler 20.03-LTS时，若仅有二进制文件而无源码，且无法使用x2openEuler工具，需解决二进制ELF文件在新系统上的依赖兼容性问题。

## 问题根因
CentOS与openEuler系统底层依赖库（如glibc等）存在差异，导致直接迁移的二进制文件因找不到对应共享库或版本不匹配而无法运行。

## 解决方案
使用patchelf工具结合自定义脚本（add-rpath.sh和expand-lib.rb）修改二进制文件及其依赖库的RPATH，将其指向在openEuler上存放的从CentOS拷贝过来的兼容库路径。具体步骤包括：安装Ruby和patchelf-0.14；创建目录存放迁移文件；通过rsync/scp拷贝二进制及依赖so文件；执行脚本设置RPATH；对缺失库使用patchelf --set-rpath指定路径。脚本获取地址：https://www.hikunpeng.com/forum/thread-0248123322153999011-1-1.html

