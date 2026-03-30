# 编译TiKV时提示找不到libclangAST.so.6的解决方法

## 内核版本


## 问题现象
在编译TiKV时，出现错误提示：'the `libclang` shared library at /usr/lib64/clang-private/libclang.so.6.0 could not be opened: libclangAST.so.6: cannot open shared object file: No such file or directory'，表明系统无法找到libclangAST.so.6动态库。

## 问题根因
libclang.so.6.0依赖于libclangAST.so.6，但该依赖库所在的路径（/usr/lib64/clang-private/）未包含在系统的动态链接器搜索路径中，导致运行时无法加载所需共享库。

## 解决方案
将libclangAST.so.6所在目录添加到LD_LIBRARY_PATH环境变量中：export LD_LIBRARY_PATH=/usr/lib64/clang-private/:$LD_LIBRARY_PATH，然后重新编译TiKV。

