# 容器里安装CANN时报错提示“Cannot fork”

## 内核版本


## 问题现象
在Ubuntu系统的容器里安装CANN软件包时，出现报错提示“Cannot fork”。

## 问题根因
容器中/bin/sh软链接指向dash而非bash，而dash在某些场景下不支持fork操作或与安装脚本不兼容。

## 解决方案
执行命令 'ls -l /bin/sh' 检查软链接指向；若指向dash，则执行 'ln -sf bash /bin/sh' 将/bin/sh修改为指向bash，然后重新执行安装命令。

