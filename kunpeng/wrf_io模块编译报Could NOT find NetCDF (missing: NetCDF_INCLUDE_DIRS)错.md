# wrf_io模块编译报Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)错

## 内核版本


## 问题现象
NCEPLIBS构建安装中wrf_io模块编译时报错：Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)。

## 问题根因
相应文件中未添加NETCDF的安装路径。

## 解决方案
1. 修改“CMakeCache.txt”文件：打开文件 /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/wrf_io/src/wrf_io-build/CMakeCache.txt，将 NetCDF_INCLUDE_DIRS 设置为正确的路径，例如 NetCDF_INCLUDE_DIRS:STRING=/path/to/NETCDF/include；2. 保存后重新执行 make 编译。

