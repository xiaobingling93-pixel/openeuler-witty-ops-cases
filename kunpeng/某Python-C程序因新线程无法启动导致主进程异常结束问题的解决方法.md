# 某Python-C程序因新线程无法启动导致主进程异常结束问题的解决方法

## 内核版本


## 问题现象
在某集群环境中，客户使用华为Donau Scheduler调度器提交大批量Python分析作业时，超过40%的作业失败。失败日志显示OpenBLAS无法创建新线程，导致主进程异常退出。

## 问题根因
OpenBLAS默认会根据物理CPU核心数启动相应数量的线程（本例中为104核），而作业提交时仅申请了1个CPU核心（-R cpu=1）。当多个作业被调度到同一节点时，每个作业仍尝试启动104个线程，导致总线程数达到104*104=10816，超过Linux系统对单个用户或进程的线程数限制，从而无法创建新线程，引发程序崩溃。

## 解决方案
在运行Python脚本时通过环境变量OMP_NUM_THREADS=1限制OpenBLAS使用的线程数，使其与作业实际申请的CPU核心数一致。例如：OMP_NUM_THREADS=1 python tools.py -f label_mol_map_atom1437 -p 2c7c_B -o data/chains7/2c7c_B.npz --res 4 --voxel_size 1.0。修改后执行40000+批量作业无失败情况。

