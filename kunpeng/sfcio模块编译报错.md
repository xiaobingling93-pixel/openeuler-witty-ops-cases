# sfcio模块编译报错

## 内核版本


## 问题现象
NCEPLIBS构建安装过程中，sfcio模块编译时报错。

## 问题根因
CMakeLists.txt中缺少对Flang Fortran编译器的处理分支，导致编译参数未正确设置。

## 解决方案
修改/nceplibs-sfcio/src/CMakeLists.txt文件，在第12行前增加对Flang编译器的支持分支：
elseif(CMAKE_Fortran_COMPILER_ID MATCHES "^(Flang)$")
  set(CMAKE_Fortran_FLAGS
      "-g -ffree-form -fconvert=big-endian -funroll-loops ${CMAKE_Fortran_FLAGS}")
  set(CMAKE_Fortran_FLAGS_RELEASE "-O2")
  set(CMAKE_Fortran_FLAGS_DEBUG "-ggdb -Wall")
保存后重新执行make编译。

