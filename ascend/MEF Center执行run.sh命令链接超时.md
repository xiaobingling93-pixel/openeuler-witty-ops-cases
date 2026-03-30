# MEF Center执行run.sh命令链接超时

## 内核版本


## 问题现象
执行run.sh命令时失败，日志显示“unable to connect to the server：Gateway Time-out”。

## 问题根因
系统代理配置问题导致kubectl无法与K8s集群建立连接。

## 解决方案
执行命令 'unset https_proxy' 禁用HTTPS代理，使用默认K8s链接。

