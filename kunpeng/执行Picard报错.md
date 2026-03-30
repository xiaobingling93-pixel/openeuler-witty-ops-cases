# 执行Picard报错

## 内核版本


## 问题现象
执行Picard时出现报错，错误信息为：“Unable to load libgkl_compression.so from native/libgkl_compression.so (/tmp/libgkl_compression8107837509941713683.so: /tmp/libgkl_compression8107837509941713683.so: cannot open shared object file: No such file or directory (Possible cause: can't load AMD 64-bit .so on a AARCH64-bit platform))”。

## 问题根因
GKL是基于Intel CPU开发的加速库，在鲲鹏（ARM架构）平台上未进行移植，导致无法加载适用于AMD64架构的共享库文件。

## 解决方案
在不涉及性能对比的情况下，该错误可以忽略。

