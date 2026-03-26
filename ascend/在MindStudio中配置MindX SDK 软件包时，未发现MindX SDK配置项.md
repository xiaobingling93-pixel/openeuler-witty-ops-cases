# 在MindStudio中配置MindX SDK 软件包时，未发现MindX SDK配置项

## 内核版本


## 问题现象
使用MindStudio配置MindX SDK，通过菜单栏“File > Settings...”打开“Settings”配置功能，在“Appearance & Behavior > System Settings”中未发现“MindX SDK”配置项。

## 问题根因
MindX SDK开发套件使用需基于CANN基础环境，需在MindStudio先配置CANN安装路径。

## 解决方案
1. 安装CANN基础环境并通过菜单栏“File > Settings...”打开“Settings”配置功能。
2. 在“Appearance & Behavior > System Settings > CANN”中配置并确认CANN安装路径。配置完成后重启MindStudio。
3. 再次进入“Settings”配置功能，在“Appearance & Behavior > System Settings”找到“MindX SDK”并完成配置。

