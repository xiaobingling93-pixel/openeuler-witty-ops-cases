# 客户端压力测试时提示chunked encoding error的解决方法

## 内核版本


## 问题现象
客户端在进行压力测试时提示“chunked encoding error”。

## 问题根因
请求压力过大，导致服务器端留存了一些缓存请求，无法正确处理分块编码（chunked encoding）的数据。

## 解决方案
调整httpress工具的并发参数（-c参数），逐步减少并发数，直到服务器端能够恢复正常响应为止。

