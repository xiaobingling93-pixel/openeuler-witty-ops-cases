# Index SDK提示报错gfortran命令未找到

## 内核版本


## 问题现象
在安装OpenBLAS时，执行编译命令 make FC=gfortran USE_OPENMP=1 –j 提示报错 gfortran：Command not found。

## 问题根因
缺失gfortran组件依赖。

## 解决方案
执行命令 apt install -y gfortran 安装gfortran工具。

