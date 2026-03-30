# 如何升级cmake？

## 内核版本


## 问题现象
操作系统自带的CMake软件版本不能满足当前数据库版本的编译要求，需要升级CMake版本。

## 问题根因


## 解决方案
1. 下载cmake-3.5.2.tar.gz上传至服务器“/home”目录。
2. 解压并进入解压后目录：
   tar -zxvf cmake-3.5.2.tar.gz
   cd cmake-3.5.2
3. 升级CMake：
   ./bootstrap
   make -j 96
   make install
4. 查看升级后CMake版本：
   /usr/local/bin/cmake --version

