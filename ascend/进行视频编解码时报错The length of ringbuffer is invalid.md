# 进行视频编解码时报错The length of ringbuffer is invalid

## 内核版本


## 问题现象
在运行InferOfflineVideo进行视频编解码时，报错“vpcDvppCommon_Init Failed.”，日志显示“CheckValid:The length of ringbuffer is invalid.”

## 问题根因
驱动固件和CANN版本不匹配

## 解决方案
根据驱动固件和CANN版本配套关系表，升级到匹配的最新驱动固件包

