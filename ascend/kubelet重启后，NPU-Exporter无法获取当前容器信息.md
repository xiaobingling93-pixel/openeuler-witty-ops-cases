# kubelet重启后，NPU-Exporter无法获取当前容器信息

## 内核版本


## 问题现象
当用户重启kubelet后，发现NPU-Exporter没有上报容器的相关信息。

## 问题根因
kubelet重启后会重新创建新dockershim.sock文件，但是NPU-Exporter获取的是旧dockershim.sock文件，导致无法获取当前容器的数据信息。

## 解决方案
可选择以下任一方式处理：方式一：无需手动处理，等待K8s自动重新拉起容器（约10秒），NPU-Exporter即可恢复正常；方式二：手动删除NPU-Exporter Pod（kubectl delete pod -n npu-exporter <npu-exporter-podname>），使其被重新拉起；方式三：修改NPU-Exporter的yaml配置，将挂载点从具体的/var/run/dockershim.sock文件改为挂载整个/var/run目录，以确保始终访问最新的sock文件。

