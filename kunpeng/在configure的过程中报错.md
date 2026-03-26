# 在configure的过程中报错

## 内核版本


## 问题现象
在configure的过程中，报错：“configure: error: liblzma development files not found”。

## 问题根因
缺少依赖包xz-devel。

## 解决方案
Python-3.8.2安装编译之前，安装xz-devel包，执行命令yum install xz-devel -y。

