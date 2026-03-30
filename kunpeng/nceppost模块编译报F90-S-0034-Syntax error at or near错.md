# nceppost模块编译报F90-S-0034-Syntax error at or near错

## 内核版本


## 问题现象
NCEPLIBS构建安装中nceppost模块报F90-S-0034-Syntax error at or near & 错误，具体出现在文件 /path/to/NCEPLIBS/NCEPLIBE-1.2.0/download/emc_post/sorc/ncep_post.fd/CMASSI.f 的第6行和第26行。

## 问题根因


## 解决方案
1. 修改“/ncep_post.fd/CMakeLists.txt”文件：打开该文件，在第188行前增加以下内容：
elseif(CMAKE_Fortran_COMPILER_ID MATCHES "^(Flang)$")
  set(CMAKE_Fortran_FLAGS "-g -ffree-form -fconvert=big-endian")
  set(CMAKE_Fortran_FLAGS_RELEASE "-O3")
  set(CMAKE_Fortran_FLAGS_DEBUG "-O0 -ggdb -fno-unsafe-math-optimizations -frounding-math -fsignaling-nans -ffpe-trap=invalid,zero,overflow -fbounds-check")
2. 保存文件后重新编译：make。

