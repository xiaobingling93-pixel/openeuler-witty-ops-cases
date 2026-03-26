# 导入torch时提示libquadmath不存在

## 内核版本


## 问题现象
在系统安装torch-1.8.1后，导入torch时出现“ImportError: libquadmath.so.0: cannot open shared object file: No such file or directory”错误。

## 问题根因
系统缺少libquadmath库这一依赖项。

## 解决方案
执行命令 `yum install libquadmath` 安装缺失的系统依赖。

