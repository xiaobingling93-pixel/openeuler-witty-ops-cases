# 使用命令行方式安装Caffe环境失败

## 内核版本


## 问题现象
使用命令行方式安装Caffe环境时，提示类似"/usr/bin/python3.7: can't open file '/usr/lib/python3.7/py_compile.py': [Error 2] No such file or directory"信息，导致Caffe环境安装失败。

## 问题根因
AMCT安装时要求先安装python3.7.5，但Caffe1.0在命令行安装过程中会查找py_compile.py文件，而该文件在python3.7.5版本中不存在（仅存在于python3.6或2.7等低版本中）。

## 解决方案
安装python3.7.5时，创建软链接：sudo ln -s /usr/local/python3.7.5/lib/python3.7 /usr/lib/python3.7；若提示链接已存在，则先执行sudo rm -rf /usr/lib/python3.7删除原有链接后再重新创建，然后重新使用命令行方式安装Caffe环境。

