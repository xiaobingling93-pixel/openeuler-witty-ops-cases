# 运行make install时报错

## 内核版本


## 问题现象
运行make install时报错，报错信息为：“Error: Array specification at (1) has more than 7 dimensions”。

## 问题根因
使用的gfortran版本过低，导致编译时环境配置不兼容。

## 解决方案
在配置环境变量时指定高版本的gfortran路径，执行命令：export FC=/path/to/GNU/bin/gfortran，然后重新编译安装。

