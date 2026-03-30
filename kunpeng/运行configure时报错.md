# 运行configure时报错

## 内核版本


## 问题现象
运行configure时报错，报错信息为：“Error: FFTW configure returned 1”。

## 问题根因
AmberTools自带的FFTW3证书已过期；运行configure时未加-nosse参数。

## 解决方案
根据报错时提示的网址去获取最新的“config.guess”和“config.sub”文件，使用vi命令更新FFTW3的“config.guess”和“config.sub”文件内容，在《AmberTools 19 移植指南（CentOS 7.6）》的“编译和安装”章节步骤8运行configure时加入“-nosse”参数。

