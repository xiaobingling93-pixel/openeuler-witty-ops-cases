# 编译过程中提示“esmump.h No such file or directory”

## 内核版本


## 问题现象
在运行Allwmake编译SCOTCH时编译失败，提示“esmump.h No such file or directory”。

## 问题根因
脚本运行中出现错误，导致esmumps没有安装成功。

## 解决方案
1. 进入scotch目录，手动编译esmumps：cd /path/to/OPENFOAM/ThirdParty-v1906/scotch_6.0.6/src，执行 make esmumps；2. 重复运行Allwmake脚本继续编译安装：foam，./Allwmake -j。

