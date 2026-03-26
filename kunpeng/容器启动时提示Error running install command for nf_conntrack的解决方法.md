# 容器启动时提示Error running install command for nf_conntrack的解决方法

## 内核版本


## 问题现象
容器启动时提示“Error running install command for nf_conntrack”。

## 问题根因
容器启动需要开启nf_conntrack模块，但该模块被blacklist.conf文件禁用。

## 解决方案
1. 打开/etc/modprobe.d/blacklist.conf文件；2. 注释掉nf_conntrack相关内容；3. 重启服务器使配置生效。

