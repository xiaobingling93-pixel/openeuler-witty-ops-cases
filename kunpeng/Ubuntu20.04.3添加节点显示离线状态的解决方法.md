# Ubuntu20.04.3添加节点显示离线状态的解决方法

## 内核版本


## 问题现象
在Ubuntu 20.04.3系统上安装系统性能分析工具后，添加节点时该节点显示为离线状态。

## 问题根因
server端环境变量no_proxy未配置，导致白名单添加失败。

## 解决方案
在server端的/etc/profile文件中添加环境变量no_proxy并使其生效：1. 执行 vi /etc/profile，添加 export no_proxy=127.0.0.1；2. 执行 source /etc/profile 使配置生效。

