# 配置device ip时报错“Failed to check the route network segment in the config file”

## 内核版本


## 问题现象
在Atlas 800 9000设备上完成驱动固件升级后，配置device ip时出现错误提示“Failed to check the route network segment in the config file. Cmd execute failed!”，同时/var/log/hccn_tool/hccn.log日志中记录“hccn tool execution failed!”。

## 问题根因
问题根因是/etc/hccn.conf配置文件缺失、内容中IP和路由配置不正确，或文件格式不符合要求。

## 解决方案
创建一个空的/etc/hccn.conf文件即可解决问题。

