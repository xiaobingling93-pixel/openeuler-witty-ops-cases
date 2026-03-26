# 程序执行若出现报错“error while loading shared libraries: libascendcl.so: cannot open shared object file: No such file or directory”

## 内核版本


## 问题现象
程序在执行过程中，出现报错：error while loading shared libraries: libascendcl.so: cannot open shared object file: No such file or directory。

## 问题根因
LD_LIBRARY_PATH环境变量中AscendCL路径配置不正确，导致系统无法找到libascendcl.so共享库文件。

## 解决方案
重新配置LD_LIBRARY_PATH环境变量，确保其中包含libascendcl.so所在的正确路径。

