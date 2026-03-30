# 鲲鹏920处理器NUMA架构中如何确认每个Socket对应的CPU？

## 内核版本


## 问题现象
在鲲鹏920处理器的NUMA架构中，用户需要确认每个物理Socket（插槽）对应哪些CPU核心和NUMA节点，以便进行性能调优或资源绑定。

## 问题根因


## 解决方案
1. 使用'lscpu'命令查看CPU架构信息，其中'Socket(s)'字段表示物理插槽数量，'NUMA nodeX CPU(s)'字段显示每个NUMA节点包含的CPU范围。例如，回显显示Socket0对应numa node0（CPU 0-31）和node1（CPU 32-63），Socket1对应node2（CPU 64-95）和node3（CPU 96-127）。2. 进一步使用'lstopo -l'命令验证，其中'Package L#0'代表第一个物理CPU插槽（Socket）。

