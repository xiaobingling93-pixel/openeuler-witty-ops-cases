# 升级MCU 3.3.4及以上版本固件包失败

## 内核版本


## 问题现象
在Atlas 300I Pro推理卡、Atlas 300V Pro视频解析卡、Atlas 300I Duo推理卡、Atlas 300V视频解析卡产品环境中，通过npu-smi工具升级MCU 3.3.4及以上版本固件包时，显示“Failed to parse file”报错。查看“/var/log/nputools_LOG_ERR.log”日志也显示相关错误信息。

## 问题根因
npu-smi工具版本与MCU固件版本不兼容。

## 解决方案
升级npu-smi工具至22.0.3及以上版本后再重新升级MCU固件。npu-smi工具集成在驱动包中，需参考《Atlas 中心推理卡 NPU驱动和固件升级指导书》进行驱动升级。升级完成后，执行npu-smi -v命令确认版本是否为22.0.3或更高。

