# wgrib2模块编译报Could NOT find JPEG和Could NOT find Jasper错

## 内核版本


## 问题现象
NCEPLIBS构建安装中wgrib2模块报错：Could NOT find JPEG (missing: JPEG_LIBRARY JPEG_INCLUDE_DIR) 和 Could NOT find Jasper (missing: JASPER_LIBRARIES JASPER_INCLUDE_DIR JPEG_LIBRARIES)。

## 问题根因
相应文件中未添加JASPER和JPEG的安装路径。

## 解决方案
1. 修改“CMakeCache.txt”文件，添加JASPER和JPEG的安装路径：
   - JASPER_INCLUDE_DIR:PATH=/path/to/JASPER/include/
   - JASPER_LIBRARY_DEBUG:FILEPATH=/path/to/JASPER/lib/
   - JASPER_LIBRARY_RELEASE:FILEPATH=/path/to/JASPER/lib/libjasper.so
   - JPEG_INCLUDE_DIR:PATH=/path/to/JPEG/include
   - JPEG_LIBRARY_DEBUG:FILEPATH=/path/to/JPEG/lib
   - JPEG_LIBRARY_RELEASE:FILEPATH=JPEG_LIBRARY_RELEASE-NOTFOUND
2. 保存文件后重新执行 make 编译。

