# 安装依赖时提示未安装或找不到Python.h

## 内核版本


## 问题现象
安装依赖时提示“fatal error：Python.h：No such file or directory”或者“Could not find <Python.h>”等信息。

## 问题根因
环境缺少Python3的开发包。

## 解决方案
根据实际使用的系统，执行以下命令安装依赖：apt-get install python3-dev；yum install python3-devel；dnf install python3-devel。

