# 解压qemu压缩包时提示tar命令不存在

## 内核版本


## 问题现象
在解压qemu压缩包时，系统提示“tar: command not found”，无法执行解压操作。

## 问题根因
系统中未安装tar工具，导致无法使用tar命令解压文件。

## 解决方案
通过yum包管理器安装tar工具，执行命令：yum -y install tar。

