# 执行do_cmake.sh和编译时报错找不到动态库的解决方法

## 内核版本


## 问题现象
执行do_cmake.sh或编译时出现错误，提示找不到动态库。具体表现为：1. CMake报错“Could Not find kps_bluestore (missing: KPS_BLUESTORE_LIBRARIES)”并提示“no libkpsbluestore.so found”；2. 链接阶段报错“cannot find -lkps_ec”，导致collect2返回链接错误。

## 问题根因


## 解决方案
1. 创建缺失的动态库软链接：执行命令 ln -snf /usr/lib64/libkps_bluestore.so.1.0.0 /usr/lib64/libkps_bluestore.so 和 ln -snf /usr/lib64/libkps_ec.so.1.2.1 /usr/lib64/libkps_ec.so；2. 清理构建目录并重新执行编译命令：rm -rf build/ && sh do_cmake.sh。

