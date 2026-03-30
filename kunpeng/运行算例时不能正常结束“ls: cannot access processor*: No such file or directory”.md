# 运行算例时不能正常结束“ls: cannot access processor*: No such file or directory”

## 内核版本


## 问题现象
算例运行一般需要几分钟，如果在一分钟内结束，查看日志文件发现错误信息：“mpirun has detected an attempt to run as root.”，导致计算无法正常进行。

## 问题根因
使用root账户运行mpirun命令时未添加允许以root身份运行的参数，导致mpirun拒绝执行。

## 解决方案
1. 执行命令 vi /path/to/OPENFOAM/OpenFOAM-v1906/bin/tools/RunFunctions 修改RunFunctions文件；
2. 在mpirun命令后增加 --allow-run-as-root 参数；
3. 保存并退出编辑；
4. 执行 ./Allclean 和 ./Allrun 重新运行算例。

