# 在MindStudio界面安装插件时提示网络未连接或插件不存在

## 内核版本


## 问题现象
启动MindStudio后，在菜单栏选择File > Settings... > Plugins搜索并安装插件时，界面提示网络未连接或插件不存在。

## 问题根因
未配置HTTP代理。

## 解决方案
配置HTTP代理：1. 在MindStudio中进入File > Settings... > Appearance & Behavior > System Settings > HTTP Proxy；2. 选择Manual proxy configuration > HTTP，填写代理服务器的Host name和Port number；3. 如需认证，勾选Proxy authentication并填写Login和Password；4. 可选勾选Remember，点击Check connection测试连接（如输入www.baidu.com）；5. 测试成功后，返回Plugins页面即可正常搜索和安装插件。

