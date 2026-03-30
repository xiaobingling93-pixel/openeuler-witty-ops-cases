# wgrib2模块编译报Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)错

## 内核版本


## 问题现象
NCEPLIBS构建安装中wgrib2模块编译时报错：Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)。

## 问题根因
相应文件中未添加NETCDF的安装路径，导致CMake无法找到NetCDF的头文件目录。

## 解决方案
1. 修改“CMakeCache.txt”文件：打开/path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/wgrib2/src/wgrib2-build/CMakeCache.txt，将NetCDF_INCLUDE_DIRS设置为实际的NetCDF include路径（如/path/to/NETCDF/include）；2. 保存后重新执行make编译。

