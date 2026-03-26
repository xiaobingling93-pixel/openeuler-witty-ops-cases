# Ceph集群PG分布不均匀的解决方法

## 内核版本


## 问题现象
在IO密集、磁盘负载较高的场景下，部分硬盘负载达到100%，而部分负载不到80%，整体磁盘负载不均衡；通过ceph pg dump发现PG分布存在优化空间。

## 问题根因
每个OSD上承载的PG数量相差过大，导致个别OSD压力较大成为性能瓶颈。

## 解决方案
使用Ceph的balancer插件进行PG分布优化：1. 通过'ceph balancer eval'或'ceph pg dump'查看当前PG分布；2. 启用自动均衡功能（'ceph balancer mode upmap'和'ceph balancer on'），系统将每隔60秒调整少量PG分布；3. 重复检查PG分布直至不再变化，表明已达到最佳状态。

