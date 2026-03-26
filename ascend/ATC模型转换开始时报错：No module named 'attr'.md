# ATC模型转换开始时报错：No module named 'attr'

## 内核版本


## 问题现象
当CANN软件包版本为6.3.RC1时，开始执行ATC模型转换时报No module named 'attr'错误信息。

## 问题根因
缺少attrs库。针对老版本镜像上重装CANN 6.3.RC1版本的软件包时，可能会缺少一些依赖库导致某些工具无法使用。

## 解决方案
安装attrs库。1. 使用命令 'pip show attrs' 查看是否已安装attrs库。2. 若未安装，使用命令 'pip install attrs' 进行安装。

