# 如何检测服务器是否支持TEE？

## 内核版本


## 问题现象
用户需要确认所使用的服务器是否支持TEE（可信执行环境）功能，以便部署基于TrustZone的机密计算应用。

## 问题根因


## 解决方案
登录服务器BIOS，依次选择“Advanced > TEE Config”查看TEE配置选项及OEMKEY安装状态。如果显示“TEE OEMKEY”处于“Install”状态，则该服务器已预置鲲鹏TrustZone套件，可通过配置“Support TEE”使能鲲鹏服务器TrustZone功能。详细信息可参考《鲲鹏BoostKit机密计算TrustZone套件 特性指南》中环境要求部分。

