# 进行MPI应用并行调试，调试失败，提示libmpi.so.40文件找不到的解决方法

## 内核版本


## 问题现象
进行MPI应用并行调试时，调试失败，报错信息为：Failed to launch lldb-server: /root/devkitdemo-devkitdemo-23.0.1/Compiler_and_Debugger/mpi_demo/kunpeng/a5459915/lldb-server: error while loading shared libraries: libmpi.so.40: cannot open shared object file: No such file or directory.

## 问题根因
系统无法找到libmpi.so.40共享库文件，可能是因为未安装对应版本的OpenMPI或环境变量未正确配置。

## 解决方案
建议安装OpenMPI 4.1.4及以上版本，并设置环境变量：export LD_LIBRARY_PATH=/opt/test/openmpi_414/lib:$LD_LIBRARY_PATH。

