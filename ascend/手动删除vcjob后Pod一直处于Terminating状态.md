# 手动删除vcjob后Pod一直处于Terminating状态

## 内核版本


## 问题现象
使用kubectl delete -f xxx.yaml删除vcjob后，对应的Pod一直处于Terminating状态，无法正常终止。

## 问题根因
Pod挂载了NFS路径，在删除vcjob后，由于NFS挂载未被正确卸载，导致Pod无法完成终止流程；此外，相关Docker进程可能仍在占用资源，进一步阻碍Pod的清理。

## 解决方案
方法一：卸载Pod的NFS挂载路径。首先通过mount|grep NFS共享IP地址查找挂载路径，然后使用umount -f命令强制卸载这些路径。方法二：若方法一无效，则需删除Pod所属的Docker进程。具体步骤包括：查找Pod对应的Docker进程，删除其在/var/lib/docker/containers下的目录，通过lsof查找并kill占用该目录的进程，最后执行docker rm删除容器。操作完成后等待约1分钟，Pod应被成功清理。

