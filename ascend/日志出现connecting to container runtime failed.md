# 日志出现connecting to container runtime failed

## 内核版本


## 问题现象
通过调用NPU-Exporter的Metrics接口（http://ip:port/metrics）无法获取NPU容器的相关信息，日志中显示错误：failed to init devices parser: connecting to container runtime failed: context deadline exceeded。

## 问题根因
NPU-Exporter启动参数“-containerd”和“-endpoint”默认配置的socket文件路径不正确，该文件在不同操作系统下位置可能不同。

## 解决方案
根据实际使用的容器运行时（Docker或containerd）调整NPU-Exporter的启动参数和yaml挂载路径：若使用Docker，需确认/var/run/dockershim.sock或相关socket路径；若使用containerd，需确认/run/containerd/containerd.sock路径是否正确，并删除yaml中名为“docker-shim”的挂载路径。可通过ps aux | grep "containerd.sock"命令查询实际sock文件路径。

