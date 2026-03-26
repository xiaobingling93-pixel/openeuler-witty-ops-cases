# 执行GATK报错

## 内核版本


## 问题现象
执行GATK时出现报错，错误信息为：“Unable to load libgkl_compression.so from native/libgkl_compression.so (/tmp/libgkl_compression8107837509941713683.so: /tmp/libgkl_compression8107837509941713683.so: cannot open shared object file: No such file or directory (Possible cause: can't load AMD 64-bit .so on a AARCH64-bit platform))”。

## 问题根因
GKL是基于Intel CPU开发的加速库，在鲲鹏（ARM架构）平台上未进行适配或移植，导致无法加载x86_64架构的共享库文件。

## 解决方案
在不涉及性能对比的场景下，该错误可以忽略；若需正常使用，应对GKL库进行针对ARM64平台的移植或使用兼容的替代方案。

