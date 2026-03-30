# nemsiogfs模块编译报错

## 内核版本


## 问题现象
NCEPLIBS构建安装过程中，nemsiogfs模块编译时报错。

## 问题根因


## 解决方案
1. 修改“/nemsiogfs.dir/build.make”文件：
   - 打开文件：vi /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/CMakeFiles/nemsiogfs.dir/build.make
   - 进入编辑模式，将第116行内容修改为：cd /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/nemsiogfs/src/nemsiogfs-build && sed -i "s/isystem/I/g" `grep -rl "isystem"` && $(MAKE)
   - 保存并退出。
2. 重新执行编译命令：make

