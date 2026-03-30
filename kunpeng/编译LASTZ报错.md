# 编译LASTZ报错

## 内核版本


## 问题现象
编译LASTZ时出现错误，报错信息为：“lastz.c:450:9: error: variable ‘freeTargetRev’ set but not used [-Werror=unused-but-set-variable]”。

## 问题根因
gcc编译时，源码Makefile中配置了“-Werror”参数，该参数会将所有警告视为错误，而代码中存在设置了但未使用的变量，触发了警告进而导致编译失败。

## 解决方案
1. 执行命令 vim src/Makefile 编辑Makefile文件；
2. 进入编辑模式后，修改CC、definedForAll和CFLAGS参数如下：
   CC=/path/to/GNU/bin/gcc
   definedForAll = -Wall -Wextra -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE
   CFLAGS = -O3 -march=armv8.2-a -mtune=tsv110 -flto ${definedForAll} ${VERSION_FLAGS}
3. 保存并退出编辑（按Esc键，输入:wq!后回车）。

