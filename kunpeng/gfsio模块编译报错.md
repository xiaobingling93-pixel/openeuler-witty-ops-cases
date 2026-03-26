# gfsio模块编译报错

## 内核版本


## 问题现象
NCEPLIBS构建安装过程中，gfsio模块编译时报错。

## 问题根因
CMakeLists.txt中缺少对Flang Fortran编译器的处理分支，导致编译参数未正确设置。

## 解决方案
修改“/nceplibs-gfsio/src/CMakeLists.txt”文件，在第8行前增加对Flang编译器的支持：
elseif(CMAKE_Fortran_COMPILER_ID MATCHES "^(Flang)$")
set(CMAKE_Fortran_FLAGS "-g -fconvert=big-endian -ffree-form ${CMAKE_Fortran_FLAGS}")
set(CMAKE_Fortran_RELEASE "-O2")
保存后重新执行make编译。

