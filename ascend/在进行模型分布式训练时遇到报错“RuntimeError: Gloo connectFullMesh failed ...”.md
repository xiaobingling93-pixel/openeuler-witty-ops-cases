# 在进行模型分布式训练时遇到报错“RuntimeError: Gloo connectFullMesh failed ...”

## 内核版本


## 问题现象
在进行模型分布式训练时，出现报错“RuntimeError: Gloo connectFullMesh failed with [...] no error”。

## 问题根因
Gloo是PyTorch原生的CPU通信协议，在存在多个网口的情况下，可能无法正确选择通信接口；此外，当bond4网口数量超过60个时，也会因Gloo协议的限制导致该错误。

## 解决方案
1. 当存在多个网口时，应通过设置环境变量指定用于Gloo通信的网口：export GLOO_SOCKET_IFNAME=网口名称（可通过ifconfig命令确认与机器IP对应的网口名称）。
2. 当bond4网口超过60个时，建议改用其他类型的网口（如GE网口），例如执行：export GLOO_SOCKET_IFNAME=enp189s0f0（其中enp189s0f0需替换为实际可用的GE网口名称）。

