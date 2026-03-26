# Volcano组件工作异常，日志出现Failed to get plugin

## 内核版本


## 问题现象
Volcano的Pod volcano-scheduler-xxxx状态为Running，但出现调度异常，日志中报错：Failed to get plugin volcano-npu_v3.0.RC2_linux-aarch64。

## 问题根因
Volcano启动配置文件（yaml）中指定的调度插件名称与实际制作镜像时拷贝进容器的插件so文件名称不一致，导致volcano-scheduler无法加载该插件。

## 解决方案
使用配套的yaml配置和对应的调度插件so文件重新制作volcano-scheduler镜像，并卸载后重新安装Volcano。

