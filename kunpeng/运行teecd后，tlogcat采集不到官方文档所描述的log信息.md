# 运行teecd后，tlogcat采集不到官方文档所描述的log信息

## 内核版本


## 问题现象
运行teecd后，tlogcat采集不到官方文档所描述的log信息，显示日志为空。

## 问题根因
tzdriver驱动未插入，导致teecd启动后立即退出，无法生成TEE日志。

## 解决方案
按照《机密计算TrustZone 特性指南》中“搭建TA和CA应用运行环境--搭建步骤”章节，先插入tzdriver驱动，再启动teecd，然后使用tlogcat查看TEE日志。

