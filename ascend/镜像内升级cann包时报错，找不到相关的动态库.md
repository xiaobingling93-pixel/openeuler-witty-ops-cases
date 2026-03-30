# 镜像内升级cann包时报错，找不到相关的动态库

## 内核版本


## 问题现象
启动镜像后，在镜像内升级cann包时提示找不到相关的动态库，导致container内操作基本无法执行，需停止并重新创建container。

## 问题根因
驱动的安装信息没有挂载到镜像内，导致镜像内cann升级时无法找到对应的动态库。

## 解决方案
在镜像启动命令中添加驱动安装信息的挂载操作，例如：-v /etc/ascend_install.info:/etc/ascend_install.info。

