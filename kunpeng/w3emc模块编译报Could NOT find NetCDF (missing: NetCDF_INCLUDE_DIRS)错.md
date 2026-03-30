# w3emc模块编译报Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)错

## 内核版本


## 问题现象
在NCEPLIBS构建安装过程中，w3emc模块编译时报错：Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)。

## 问题根因
相应文件中未添加NETCDF的安装路径。

## 解决方案
1. 修改“CMakeCache.txt”文件：打开文件 /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/w3emc/src/w3emc-build/CMakeCache.txt，进入编辑模式，将 NetCDF_INCLUDE_DIRS 设置为正确的 NETCDF include 路径，例如 NetCDF_INCLUDE_DIRS:STRING=/path/to/NETCDF/include；保存并退出。2. 重新执行 make 编译命令。

