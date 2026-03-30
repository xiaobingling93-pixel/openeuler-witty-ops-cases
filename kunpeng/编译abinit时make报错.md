# 编译abinit时make报错

## 内核版本


## 问题现象
编译abinit时make报错，报错信息为：“File 'mpi.mod' opened at (1) is not a GNU Fortran module file”。

## 问题根因
gcc和OpenMPI编译器版本不对应。

## 解决方案
统一OpenMPI和ABINIT使用的编译器可以解决问题。

