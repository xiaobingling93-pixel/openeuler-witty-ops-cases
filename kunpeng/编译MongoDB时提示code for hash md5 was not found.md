# 编译MongoDB时提示code for hash md5 was not found

## 内核版本


## 问题现象
编译MongoDB时提示“ERROR:root:code for hash md5 was not found.”。

## 问题根因
Python没有成功安装hashlib模块。

## 解决方案
1. 下载hashlib源码包，并对hashlib进行编译安装：
wget https://files.pythonhosted.org/packages/74/bb/9003d081345e9f0451884146e9ea2cff6e4cc4deac9ffd4a9ee98b318a49/hashlib-20081119.zip
unzip hashlib-20081119.zip
cd hashlib-20081119
python2 setup.py install
2. 重新编译MongoDB。

