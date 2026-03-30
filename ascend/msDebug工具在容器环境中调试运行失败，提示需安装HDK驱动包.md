# msDebug工具在容器环境中调试运行失败，提示需安装HDK驱动包

## 内核版本


## 问题现象
在容器环境中运行msDebug工具进行调试时失败，提示“msdebug failed to initialize. please install HDK with --debug before debugging”。

## 问题根因
未使用--debug选项安装HDK驱动包，或msDebug工具依赖的驱动设备节点/dev/drv_debug未映射至容器环境内。

## 解决方案
1. 检查宿主机是否已使用--debug选项安装HDK驱动包，确认是否存在/dev/drv_debug设备节点；2. 若在容器环境中运行，需在容器启动命令中添加--privileged --device=/dev/drv_debug选项，以确保调试所需的设备节点被正确映射并具备访问权限。

