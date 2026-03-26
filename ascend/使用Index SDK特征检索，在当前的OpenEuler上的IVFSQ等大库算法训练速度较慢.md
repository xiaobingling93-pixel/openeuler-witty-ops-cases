# 使用Index SDK特征检索，在当前的OpenEuler上的IVFSQ等大库算法训练速度较慢

## 内核版本
openEuler release 20.03 (LTS)

## 问题现象
在当前的OpenEuler系统上，使用Index SDK进行特征检索时，IVFSQ等大库算法的训练速度较慢。

## 问题根因
OpenEuler release 20.03 (LTS) 上由于GOMP开关引入了CPU性能劣化的bug。

## 解决方案
可以参考指定链接（https://gitee.com/src-openeuler/openEuler-release/pulls/55）中的改动进行修改和适配，或升级到最新版本的OpenEuler系统。

