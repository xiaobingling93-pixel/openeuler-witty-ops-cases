# Index在执行查询操作时，出现性能波动

## 内核版本


## 问题现象
执行查询操作时，当查询的条数大于100时，出现了性能波动。

## 问题根因
Host侧CPU并发处理时，调度到非亲和性的CPU核上，导致耗时增加。

## 解决方案
需对检索应用进行绑核操作：1. 获取NPU所属的NUMA node信息；2. 使用lscpu命令查看该NUMA node对应的CPU核范围；3. 使用taskset命令将检索应用绑定到对应的CPU核上，例如：taskset -c 0-13,28-41 ./mxIndexApp（其中mxIndexApp需替换为实际应用名称）。

