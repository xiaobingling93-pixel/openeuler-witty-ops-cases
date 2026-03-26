# 执行编译安装Tengine命令时提示ngx_murmurhash.c的解决方法

## 内核版本


## 问题现象
执行编译安装Tengine的命令时提示“src/core/ngx_murmurhash.c”，导致编译失败。

## 问题根因
编译过程中出现警告信息，而Makefile中启用了“-Werror”选项，将警告视为错误，从而导致编译中断。

## 解决方案
1. 打开Makefile文件：vim objs/Makefile；
2. 进入编辑模式，删除CFLAGS中的“-Werror”；
3. 保存并退出；
4. 重新执行编译安装命令：make && make install。

