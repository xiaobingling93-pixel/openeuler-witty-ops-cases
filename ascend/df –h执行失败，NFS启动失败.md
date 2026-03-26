# df –h执行失败，NFS启动失败

## 内核版本


## 问题现象
执行df –h命令失败；使用strace df –h查看发现命令卡住；重启NFS服务时提示“Job for nfs-server.service canceled”，服务启动失败。

## 问题根因
NFS共享配置文件/etc/exports中指定的共享目录（/data/atlas_dls）在系统中不存在，导致NFS服务无法正常启动，进而使df –h命令因等待NFS响应而卡住。

## 解决方案
创建缺失的共享目录：mkdir /data/atlas_dls；然后重启NFS服务：sudo /etc/init.d/nfs-kernel-server start；之后df –h命令可正常执行。

