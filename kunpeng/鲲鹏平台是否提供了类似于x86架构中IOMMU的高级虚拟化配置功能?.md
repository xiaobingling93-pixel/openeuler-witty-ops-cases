# 鲲鹏平台是否提供了类似于x86架构中IOMMU的高级虚拟化配置功能?

## 内核版本


## 问题现象
用户询问鲲鹏平台是否提供类似x86架构中IOMMU的高级虚拟化配置功能。

## 问题根因
鲲鹏架构使用SMMU（System Memory Management Unit）来实现类似x86架构中IOMMU（Input/Output Memory Management Unit）的功能，用于处理虚拟化环境中多个虚拟机或容器对系统内存的访问。

## 解决方案
鲲鹏架构中的SMMU可替代x86中的IOMMU功能。SMMU在BIOS中的配置方法请参见《TaiShan 服务器 BIOS 参数参考（鲲鹏920处理器）》。

