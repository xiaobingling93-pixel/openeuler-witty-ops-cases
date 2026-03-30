# MindSDK案例执行失败：owner id diff

## 内核版本


## 问题现象
在Ubuntu18.04系统、CANN 6.0.RC1环境下，执行MindSDK推理案例时出现两个问题：1）提示权限问题（owner id diff）；2）提示插件mxpi_classpostprocessor0不存在。

## 问题根因
问题1：镜像中默认安装的MindSDK应用程序所有者为hwMindx用户，但实际以root用户启动程序，导致权限不匹配。问题2：pipeline配置文件中mxpi_classpostprocessor0插件的路径配置错误，导致系统无法找到该插件。

## 解决方案
问题1：在容器中重新安装MindSDK，确保程序所有者与运行用户一致。问题2：修改pipeline配置文件中mxpi_classpostprocessor0插件的路径为正确路径。

