# 使用源码方式编译KAE时提示cannot create regular file的解决方法

## 内核版本


## 问题现象
源码方式编译安装鲲鹏加速引擎时，执行make命令，提示无法创建普通文件，即build软连接所指向的目录不存在的错误，具体信息为：“cannot create regular file '...': No such file or directory”。

## 问题根因
系统中没有安装kernel-devel或安装的kernel-devel软件包与OS的内核版本不匹配，导致build软连接所指向的内核头文件目录不存在。

## 解决方案
检查系统中是否已安装kernel-devel或安装的kernel-devel软件包与OS的内核版本是否匹配。若已安装但版本不匹配，执行命令“yum install kernel-devel-$(uname -r)”重新安装；若未安装，则同样执行该命令完成安装。

