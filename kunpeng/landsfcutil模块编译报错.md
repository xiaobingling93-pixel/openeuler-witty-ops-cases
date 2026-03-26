# landsfcutil模块编译报错

## 内核版本


## 问题现象
NCEPLIBS构建安装中landsfcutil模块编译时报错，具体错误信息见图片：/doc_center/source/zh/kunpenghpcs/hpcindapp/trouble/zh-cn_image_0000001208283374.png。

## 问题根因
CMakeLists.txt文件中缺少对flang编译器的处理分支，导致使用flang编译时无法正确设置Fortran编译选项。

## 解决方案
修改“/nceplibs-landsfcutil/src/CMakeLists.txt”文件，在第11行前增加对Flang编译器的支持分支：
elseif(CMAKE_Fortran_COMPILER_ID MATCHES "^(Flang)$")
  set(CMAKE_Fortran_FLAGS "-g -ffree-form ${CMAKE_Fortran_FLAGS}")
  set(CMAKE_Fortran_FLAGS_RELEASE "-O3")
  set(CMAKE_Fortran_FLAGS_DEBUG "-ggdb -Wall")
  set(fortran_d_flags "-fdefault-real-8")
保存后重新执行make编译。参考修改示意图片：/doc_center/source/zh/kunpenghpcs/hpcindapp/trouble/public_sys-resources/note_3.0-zh-cn.png。

