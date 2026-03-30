# 容器创建IPVlan网络时提示plugin "ipvlan" not found的解决方法

## 内核版本


## 问题现象
容器创建IPVlan网络时，提示“plugin \"ipvlan\" not found”。

## 问题根因
容器默认不支持IPVlan，需要启用Docker的实验性功能（experimental features）才能使用ipvlan插件。

## 解决方案
1. 打开“daemon.json”文件：vi /etc/docker/daemon.json
2. 在“daemon.json”文件中，将experimental字段后的值改为true，例如：{"experimental": true}
3. 重启Docker服务：systemctl restart docker

