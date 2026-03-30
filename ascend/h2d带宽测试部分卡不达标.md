# h2d带宽测试部分卡不达标

## 内核版本


## 问题现象
h2d带宽测试中，部分加速卡的测试结果未达到预期带宽标准。

## 问题根因
未在BIOS中使能One Numa Per Socket选项，导致4个CPU共用一个NUMA Node，部分CPU访问非本地内存时带宽受限，从而影响h2d（Host to Device）带宽性能。

## 解决方案
进入服务器BIOS设置，找到Memory Config选项，启用One Numa Per Socket功能，使每个CPU对应独立的NUMA Node，优化内存访问路径，提升带宽表现。

