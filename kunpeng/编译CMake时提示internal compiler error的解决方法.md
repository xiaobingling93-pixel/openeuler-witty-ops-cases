# 编译CMake时提示internal compiler error的解决方法

## 内核版本


## 问题现象
在鲲鹏服务器CentOS 7.6操作系统上安装KVM虚拟机，分配20vCPU、3GB内存的情况下，执行make -j 20命令编译CMake时，提示“g++: internal compiler error: Killed (program cc1plus)”。

## 问题根因
虚拟机内存不足且未配置SWAP分区，导致编译过程中因资源耗尽被系统终止。

## 解决方案
增加虚拟机内存至16GB：1. 执行virsh edit mysql编辑虚拟机配置；2. 修改内存为16GB；3. 重启虚拟机（virsh shutdown mysql 和 virsh start mysql）；4. 重新编译CMake成功。

