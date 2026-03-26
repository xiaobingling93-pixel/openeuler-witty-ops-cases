# 导入torch时提示libblas不存在

## 内核版本


## 问题现象
系统安装torch-1.8.1后，在导入torch时出现“ImportError: libblas.so.3: cannot open shared object file: No such file or directory”错误。

## 问题根因
系统未安装openblas依赖，导致libblas.so.3库文件缺失。

## 解决方案
1. 执行命令安装openblas依赖：yum install openblas；2. 查找系统中libopenblas的so文件（如libopenblas-r0.3.9.so）；3. 创建软链接：ln -s /usr/lib64/libopenblas-r0.3.9.so /usr/lib64/libblas.so.3 和 ln -s /usr/lib64/libopenblas-r0.3.9.so /usr/lib64/liblapack.so.3。

