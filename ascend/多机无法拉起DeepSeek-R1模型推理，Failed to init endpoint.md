# 多机无法拉起DeepSeek-R1模型推理，Failed to init endpoint

## 内核版本


## 问题现象
MindIE推理启动服务时出现错误提示：Failed to init endpoint! Please check the service log or console output。

## 问题根因
开启了HTTPS（httpsEnabled设置为true），但未正确配置证书。

## 解决方案
1. 若httpsEnabled为true，请检查并正确配置证书，参考MindIE社区文档；2. 或将httpsEnabled修改为false。

