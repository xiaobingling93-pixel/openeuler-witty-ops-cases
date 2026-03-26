# 升级CANN包时报错：unable to get driver config file

## 内核版本


## 问题现象
在容器内执行--upgrade升级CANN包时，报错提示：unable to get driver config file /usr/local/Ascend/driver/version.info。

## 问题根因
可能原因包括：1. driver/version.info驱动文件被删除，或者容器环境没有映射宿主机的driver文件夹；2. 驱动卸载流程不正确。

## 解决方案
将宿主机的driver/version.info文件拷贝到容器对应目录，例如执行命令：docker cp /usr/local/Ascend/driver/version.info container_id:/usr/local/Ascend/driver/，其中container_id为容器ID，可通过docker ps -a命令查看。

