# 鲲鹏DevKit的HPC应用分析怎么对py文件分析？

## 内核版本


## 问题现象
用户尝试使用鲲鹏DevKit的HPC应用分析功能对Python（.py）文件进行分析，但无法成功。

## 问题根因
HPC应用分析功能仅面向OpenMP和MPI应用，要求以mpirun命令启动，而Python文件不属于该工具支持的分析对象。

## 解决方案
HPC应用分析不支持直接分析Python文件。如需分析，应确保目标应用为基于OpenMP或MPI的并行程序，并通过mpirun命令启动，例如：mpirun -n 4 devkit tuner hpc-perf -L summary <command> [<options>]。

