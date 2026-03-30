# 程序调用KAE时提示wd pool无法初始化

## 内核版本


## 问题现象
在某些环境上运行程序调用KAE时会报错，提示“dma_num = x, not enough. failed to initialize wd pool.”，即wd pool无法初始化。

## 问题根因
环境上可用的CMA（Contiguous Memory Allocator）空间不足，导致程序无法申请到足够大的连续内存。

## 解决方案
如果关闭SMMU使用KAE，需要保证CMA内存空间充足；否则建议开启SMMU，通过SMMU将离散内存映射成连续内存。开启SMMU的方式请参见BIOS配置文档。

