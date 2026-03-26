# 安装依赖“broom”失败

## 内核版本


## 问题现象
在安装MWASTools过程中，提示类似ERROR：dependencies ‘stringr’，‘ggplot2’ are not available for package ‘broom’的报错，导致依赖“broom”安装失败。

## 问题根因
因网络超时或依赖版本与Bioconductor不匹配等原因，导致安装依赖“broom”的子依赖“stringr”和“ggplot2”失败，从而引发“broom”安装失败。

## 解决方案
方法一：通过命令 BiocManager::install("stringr") 和 BiocManager::install("ggplot2") 优先安装子依赖，完成后再次执行 BiocManager::install("broom")。方法二：若方法一失败，可手动下载stringr源码（根据报错提示获取源码地址），并通过 R CMD INSTALL xxxxx.tar.gz 命令进行本地安装。

