# 当前Kbox云手机容器支持哪些处理器型号，如何配置？

## 内核版本


## 问题现象
用户需要了解Kbox云手机容器支持的处理器型号以及相应的配置方法。

## 问题根因


## 解决方案
Kbox云手机容器支持鲲鹏920 7260Y/7265/7260处理器。具体配置需根据不同的使用需求修改“cfct_config”文件中的相关变量，例如编码卡类型（ENCODECARD）、GPU映射（VIDEO_GPU_MAP_AMD1/AMD2）、CPU绑核方式（CPU_BIND_MODE）、内存存储大小（RAM_SIZE_GB、STORAGE_SIZE_GB）及分辨率帧率（BUILD_WIDTH、BUILD_HEIGHT、BUILD_DENSITY、BUILD_FPS）等。同时提供了两种基础云手机规格及其对应的硬件配置建议，包括CPU、内存、硬盘、网卡、Riser卡、编码卡和GPU等详细参数。

