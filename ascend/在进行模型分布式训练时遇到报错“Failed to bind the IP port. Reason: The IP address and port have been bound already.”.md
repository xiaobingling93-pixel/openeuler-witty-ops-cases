# 在进行模型分布式训练时遇到报错“Failed to bind the IP port. Reason: The IP address and port have been bound already.”

## 内核版本


## 问题现象
在进行模型分布式训练时，系统报错：“Failed to bind the IP port. Reason: The IP address and port have been bound already.”，具体错误信息显示HCCL组件尝试绑定端口（如60007）失败，原因是该IP地址和端口已被占用。

## 问题根因
HCCL组件在分布式训练中默认使用60000~60015端口进行集群通信，若这些端口已被其他进程占用，或操作系统未将这些端口预留，则会导致端口绑定失败。

## 解决方案
需要为HCCL预留所需端口范围。若仅需临时生效，可执行命令：sysctl -w net.ipv4.ip_local_reserved_ports=60000-60015；若需永久生效，则需编辑/etc/sysctl.conf文件，在末尾添加net.ipv4.ip_local_reserved_ports=60000-60015，并执行sysctl -p使配置生效。如果通过环境变量HCCL_IF_BASE_PORT指定了起始端口，则应预留从该端口开始的连续16个端口。

