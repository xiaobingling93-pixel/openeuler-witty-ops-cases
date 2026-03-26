# MindIE Benchmark使用Client推理模式运行时出现HTTPS连接错误

## 内核版本


## 问题现象
MindIE Benchmark使用Client推理模式运行时出现HTTPS连接错误，而curl命令可以正常发送请求。

## 问题根因
config.json中配置的managementIpAddress和managementPort与benchmark命令中--ManagementHttp参数不匹配。

## 解决方案
如果用户修改了config.json中的managementIpAddress和managementPort配置，应根据实际配置值正确设置--ManagementHttp参数。

