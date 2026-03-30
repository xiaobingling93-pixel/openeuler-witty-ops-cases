# openEuler操作系统运行MPI+OpenMP精细化分析为何失败？

## 内核版本


## 问题现象
在openEuler操作系统中运行MPI+OpenMP精细化分析失败。

## 问题根因
openEuler操作系统中自带的MPI工具为低版本MPICH，而HPC应用分析任务仅支持MPICH 4.0.3及其以上版本。

## 解决方案
升级系统中的MPICH至4.0.3或更高版本以满足HPC应用分析任务的要求。

