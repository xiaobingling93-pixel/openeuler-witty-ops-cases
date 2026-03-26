# 使用错误的DVPP内存申请接口，导致应用程序报错并退出

## 内核版本


## 问题现象
应用程序运行时报错并退出，日志中显示“input buffer is invalid”和“output buffer is invalid”，提示需使用hi_mpi_dvpp_malloc或acldvppMalloc接口分配内存。

## 问题根因
DVPP媒体数据处理对输入输出内存有特殊要求（如128字节对齐），但代码中未使用指定的专用接口（acldvppMalloc用于V1版本，hi_mpi_dvpp_malloc用于V2版本）申请Device内存，导致内存地址校验失败。

## 解决方案
检查代码，确保在DVPP媒体数据处理功能中使用acldvppMalloc或hi_mpi_dvpp_malloc接口申请输入/输出Device内存；其他非DVPP功能建议使用aclrtMalloc申请内存以避免占用DVPP专用地址空间。

