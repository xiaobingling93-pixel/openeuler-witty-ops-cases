# wrf_io模块编译报F90-S-0017-Unable to open include file: netcdf.inc错

## 内核版本


## 问题现象
NCEPLIBS构建安装中wrf_io模块编译时报错：F90-S-0017-Unable to open include file: netcdf.inc。

## 问题根因


## 解决方案
1. 修改“/wrf_io.dir/build.make”文件：打开该文件，将第115行内容替换为：cd /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/wrf_io/src/wrf_io-build && sed -i "s/isystem/I/g" `grep -rl "isystem"` && $(MAKE)；2. 保存后重新执行make命令进行编译。

