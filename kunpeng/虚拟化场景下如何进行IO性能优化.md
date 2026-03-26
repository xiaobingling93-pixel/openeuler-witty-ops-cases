# 虚拟化场景下如何进行IO性能优化

## 内核版本


## 问题现象
在鲲鹏服务器下进行虚拟机（8C16G）裸盘（预分配80G）fio 4k随机写测试（4jobs，iodepth为32）时，性能不符合预期。

## 问题根因
问题根因包括：1）磁盘类型使用virtio-scsi-device导致KVM线程数过多和虚拟机cpu0软中断过高；2）QEMU版本较低，不支持ARMv8新特性；3）未启用virtio-blk多队列特性，导致单核瓶颈；4）物理机SSD调度策略为默认cfq，未优化；5）异步IO模式未配置为native，影响性能。

## 解决方案
1. 使用最新版本的QEMU，并尽量使用更高版本的Guest OS；2. 将磁盘类型调整为virtio-block-device并启用multiqueues多队列特性；3. 将虚拟机异步IO模式配置为native；4. 将物理机SSD调度策略由cfq调整为noop；5. 若无需磁盘、网卡直通或SRIOV特性，可关闭SMMU；6. 在分析性能瓶颈时，需同时结合虚拟机和物理机的系统表现进行综合判断。

