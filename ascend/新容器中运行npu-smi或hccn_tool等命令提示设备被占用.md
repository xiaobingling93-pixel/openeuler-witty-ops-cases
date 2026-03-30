# 新容器中运行npu-smi或hccn_tool等命令提示设备被占用

## 内核版本


## 问题现象
在Atlas系列AI硬件的新启动容器中执行npu-smi或hccn_tool等命令时，提示设备被占用，报错信息为“dcmi model initialized failed, because the device is used. ret is -8020”。

## 问题根因
设备被占用的原因包括：1）存在另一个普通容器正在使用这些设备；2）宿主机上存在与pid为1的进程“mount namespace”不同的进程正在使用这些设备；3）存在一个曾使用非root用户运行过的特权容器。

## 解决方案
1. 在宿主机执行cat /proc/uda/namespace_node命令，根据ns_id小于128的映射表找到被占用设备对应的root_tgid（使用进程）。2. 若该进程属于宿主机，直接退出；若属于容器，通过ps -ef结合container id定位并退出对应容器。若多个容器占用目标设备，则需全部退出后，新容器才能正常使用设备。

