# 解决htcondor在鲲鹏920上启动服务失败

## 内核版本


## 问题现象
HTCondor在鲲鹏920上启动服务失败。

## 问题根因
默认的栈大小（stack_size）不足以支持在鲲鹏920架构上通过clone()创建子进程，导致服务启动失败。

## 解决方案
修改源码文件 condor-8.9.2/src/condor_daemon_core.V6/daemon_core.cpp 中第5856-5880行，将 stack_size 从默认值（如16384）增大到 64*1024*2（即128KB），并确保栈指针对齐。具体操作为：编辑 daemon_core.cpp 文件，找到相关代码段，取消注释并调整 stack_size 的定义，保存后重新编译安装。

