# 片上内存压测失败，日志报aclopRegisterCompileFunc failed

## 内核版本


## 问题现象
使用片上内存压测时，压测失败，结果为fail。日志中报错：[ERROR]...[hbm_stress.cpp xxxxxx] aclopRegisterCompileFunc failed, error code: 100030, device: 4。使用的环境为驱动23.0.5.1、固件7.1.0.8.220、Toolkit 8.0.RC2、MindCluster ToolBox 5.0.1。

## 问题根因
CANN包在8.0.RC2版本中已更新升级片上内存压测的算子，其与6.0.RC1及以前版本的MindCluster ToolBox输入不匹配，导致片上内存压测失败。

## 解决方案
请使用配套版本的CANN和MindCluster ToolBox进行片上内存压测，如CANN 8.0.RC2 版本和MindCluster ToolBox 6.0.RC2及以上版本。

