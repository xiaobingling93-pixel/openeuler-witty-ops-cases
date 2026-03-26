# Fortran程序迁移至鲲鹏平台时提示REAL*10 not supported的解决方法

## 内核版本


## 问题现象
在将Fortran程序迁移至鲲鹏平台时，编译过程中出现错误：'Old-style type declaration REAL*10 not supported'，导致编译失败。

## 问题根因
x86服务器的FPU寄存器包含8个80位数据寄存器，因此在x86架构上GFortran支持REAL*10类型；而鲲鹏平台（ARM架构）的GFortran不支持REAL*10这种数据长度，因此编译时报错。

## 解决方案
将代码中的REAL*10类型修改为REAL*8类型以兼容鲲鹏平台的编译器。

