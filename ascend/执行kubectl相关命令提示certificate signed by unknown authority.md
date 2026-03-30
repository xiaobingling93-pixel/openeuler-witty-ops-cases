# 执行kubectl相关命令提示certificate signed by unknown authority

## 内核版本


## 问题现象
执行kubectl相关命令（如 kubectl get pods --all-namespaces）时，提示错误：Unable to connect to the server: x509: certificate signed by unknown authority。

## 问题根因
环境配置了代理，导致kubectl在连接Kubernetes API服务器时无法验证证书颁发机构。

## 解决方案
执行 unset http_proxy https_proxy 命令取消代理设置，以恢复kubectl与API服务器的正常通信。

