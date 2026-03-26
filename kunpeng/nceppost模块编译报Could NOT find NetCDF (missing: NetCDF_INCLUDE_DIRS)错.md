# nceppost模块编译报Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)错

## 内核版本


## 问题现象
NCEPLIBS构建安装过程中，nceppost模块编译时报错：Could NOT find NetCDF (missing: NetCDF_INCLUDE_DIRS)。

## 问题根因
相应文件中未添加NetCDF的安装路径，导致CMake无法找到NetCDF的头文件目录。

## 解决方案
1. 修改“CMakeCache.txt”文件：打开/path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/nceppost/src/nceppost-build/CMakeCache.txt；
2. 在文件中添加NetCDF_INCLUDE_DIRS:STRING=/path/to/NETCDF/include；
3. 保存文件后重新执行make命令进行编译。

