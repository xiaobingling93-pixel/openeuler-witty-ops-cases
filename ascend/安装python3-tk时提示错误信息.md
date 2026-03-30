# 安装python3-tk时提示错误信息

## 内核版本


## 问题现象
安装python3-tk依赖时，提示错误信息：'[Errno 2] No such file or directory dpkg ...'。

## 问题根因
缺少py_compile.py文件导致安装失败。

## 解决方案
将缺失的文件py_compile.py复制到/usr/lib/python3.7路径，然后重新安装。具体命令为：cp /usr/local/python3.7.5/lib/python3.7/py_compile.py /usr/lib/python3.7（请根据实际路径替换源文件位置）。

