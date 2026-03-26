# 编译libfms.a时报错

## 内核版本


## 问题现象
编译libfms.a时报错，报错信息为：“Package mpich2 was not found in the pkg-config search path”。

## 问题根因
linux-gnu.mk中mpich2参数未修改。

## 解决方案
执行以下命令修改“linux-gnu.mk”文件：
cd /path/to/MOM/MOM6-examples/src/mkmf/templates/
sed -ri 's/mpich2/ompi/g' linux-gnu.mk

