# 容器创建IPVlan网络失败的解决方法

## 内核版本


## 问题现象
容器创建IPVLAN网络失败，提示“plugin "ipvlan" not found”。

## 问题根因
容器默认不支持IPVLAN，需要启用Docker的实验性功能以支持IPVLAN插件。

## 解决方案
1. 编辑daemon.json文件：vim /etc/docker/daemon.json
2. 添加配置字段：{"experimental": true}
3. 保存并退出编辑。
4. 重启docker服务。

