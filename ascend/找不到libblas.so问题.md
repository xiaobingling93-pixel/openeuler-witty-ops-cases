# 找不到libblas.so问题

## 内核版本


## 问题现象
系统在运行过程中报错找不到libblas.so库文件。

## 问题根因
环境缺少openblas库，导致无法找到libblas.so。

## 解决方案
在CentOS或EulerOS环境中执行 'yum -y install openblas'；在Ubuntu环境中执行 'apt install libopenblas-dev' 来安装缺失的openblas库。

