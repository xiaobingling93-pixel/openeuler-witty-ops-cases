# 运行runProof时报错

## 内核版本


## 问题现象
运行runProof("simple(nevt=10000000000000000,nhist=100)")时报错，报错信息为：“SysError in <TUnixSystem::UnixTcpConnect>: connect (localhost:40000) (Connection refused)”。

## 问题根因
在服务器本地运行时，不需要启动xproofd守护进程。

## 解决方案
运行时加入"lite://"参数。

