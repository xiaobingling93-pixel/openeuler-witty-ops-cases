# 编译Geant4并行模块时报错

## 内核版本


## 问题现象
编译Geant4并行模块时报错，报错信息为：“G4MPImanager.hh:117:9: error: ‘MPI’ does not name a type; did you mean ‘M_PI’?”。

## 问题根因
OpenMPI 4.0.1默认没有打开g++绑定。

## 解决方案
重新编译OpenMPI 4.0.1并在配置OpenMPI时加入--enable-mpi-cxx参数，详细操作请参见《鲲鹏BoostKit HPC使能套件-安装指南（开源组件）》中“基础环境搭建指南 > 集群场景环境搭建 > OpenMPI安装”。

