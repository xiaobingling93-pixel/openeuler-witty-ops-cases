# MEF Edge执行run.sh命令失败

## 内核版本


## 问题现象
run.sh命令在具有可执行权限（x权限）的情况下仍然执行失败，系统回显“Permission denied”。

## 问题根因
当前路径的挂载点可能设置了noexec参数，导致无法在此路径下执行任何命令。

## 解决方案
方法一：更换至未设置noexec参数的路径下安装软件并运行；方法二：使用bash命令直接执行脚本，例如：bash ./run.sh start。

