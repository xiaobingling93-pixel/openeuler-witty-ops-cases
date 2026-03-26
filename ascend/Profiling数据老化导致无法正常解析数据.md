# Profiling数据老化导致无法正常解析数据

## 内核版本


## 问题现象
当Profiling数据超过storage_limit参数限定的最大值或剩余磁盘空间较小时，Profiling会自动老化并删除最早的Profiling数据，导致在未指定--iteration-id或指定已被删除的早期迭代ID进行解析时，解析失败。

## 问题根因
Profiling数据老化机制默认从--iteration-id=1开始删除旧数据，而解析操作若未明确指定有效的迭代ID（如仍使用默认从1开始），则会因对应数据已被删除而失败。

## 解决方案
1. 执行命令 ./msprof --query=on --output=<dir> 查看最大迭代轮数（Iteration Number）；2. 解析时指定迭代ID最大的Profiling数据以确保数据存在。

