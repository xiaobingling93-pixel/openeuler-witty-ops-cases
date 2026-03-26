# 编译时报“fatal error: 'hb.h' file not found”错误

## 内核版本


## 问题现象
编译时出现错误：/usr/include/pango-1.0/pango/pango-coverage.h:28:10: fatal error: 'hb.h' file not found #include <hb.h>，系统无法找到头文件“hb.h”。

## 问题根因


## 解决方案
1. 使用命令 `find -name hb.h` 在 /usr 目录下查找 hb.h 所在路径；
2. 编辑 Makefile 文件（例如：/path/to/PyFerret/PyFerret-7.6.0/fer/cferbind/Makefile），在第17行添加 `-I/usr/include/harfbuzz` 以指定头文件搜索路径；
3. 保存修改后，执行 `make clean` 和 `make` 重新编译项目。

