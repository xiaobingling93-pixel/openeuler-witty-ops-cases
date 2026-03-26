# 编译abinit时make报错

## 内核版本


## 问题现象
编译abinit时make报错，报错信息为：“abinit-8.10.3/config/gnu/missing: line 81: automake-1.16: command not found”。

## 问题根因
此错误是因为生成Makefile时指定了aclocal和automake版本为1.16，而系统中未安装该版本的automake。

## 解决方案
查看系统的automake版本，并在Makefile中替换成系统实际安装的版本。具体操作：编辑“abinit-8.10.3/build/Makefile”文件，将“automake-1.16”修改为系统中存在的automake版本，保存后重新执行make命令。

