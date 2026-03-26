# boost安装过程中报错

## 内核版本


## 问题现象
运行./b2 install后报错，报错信息：“gcc: error: unrecognized command line option ‘-m64’”。

## 问题根因
-m64是x86 64位应用编译选项，用于为AMD的x86 64架构生成代码，在ARM64平台无法支持。

## 解决方案
执行以下命令修改boost中的源码，将ARM64平台对应的编译选项设置为-mabi=lp64：sed -ri 's/\-m64/\-mabi=lp64/g' `grep -Rl '\-m64'`

