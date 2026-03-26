# 芯片无法正常启动，系统日志报NVME协议地址未4K对齐

## 内核版本


## 问题现象
在Atlas 200I A2加速模块环境中，芯片无法正常启动，系统日志打印信息：dev id 0, The address dont comply with the NVME protocol(must be aligned with 4KB)。

## 问题根因
Host内核接口dma_alloc_coherent申请用于NVMe协议的地址不满足4K对齐要求。可能原因包括：用户内核PAGESIZE小于4096字节，或dma_alloc_coherent的实现方式与Linux社区标准不一致。

## 解决方案
执行getconf PAGESIZE命令查询当前环境页大小。若PAGESIZE小于4096字节，需修改Host内核或调整PAGESIZE；若PAGESIZE大于等于4096字节，则需排查dma_alloc_coherent接口实现，确保其返回的地址满足4K对齐要求。

