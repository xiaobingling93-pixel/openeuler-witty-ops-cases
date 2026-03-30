# 基于MindX SDK开发应用，使用MindX SDK Pipeline功能查看可视化pipeline时，发现插件变灰

## 内核版本


## 问题现象
在MindStudio中开发基于MindX SDK应用，使用MindX SDK Pipeline功能查看可视化pipeline时，发现其中部分或全部插件变灰。

## 问题根因
MindStudio在启动时未获取到插件在库中的文件路径。

## 解决方案
若当前pipeline未使用自定义插件，需重新配置并生效SDK环境变量，执行如 source $HOME/Ascend/mindx_sdk/mxManufacture_{version}/linux-{arch}/mxManufacture/set_env.sh 或 source $HOME/Ascend/mindx_sdk/mxVision_{version}/linux-{arch}/mxVision/set_env.sh 的命令；若存在自定义插件，则通过MindX SDK Pipeline中的Plugin Manager功能导入权限为440的自定义插件目录，然后重新打开pipeline以加载插件。

