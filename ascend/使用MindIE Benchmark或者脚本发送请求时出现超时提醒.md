# 使用MindIE Benchmark或者脚本发送请求时出现超时提醒

## 内核版本


## 问题现象
使用MindIE Benchmark或者脚本对MindIE Server发送请求时，部分请求出现超时且无返回的情况。

## 问题根因
发送请求速率超过服务化所能处理请求的能力，导致请求积压，从而引发返回超时。

## 解决方案
若使用MindIE Benchmark，应降低并发数（即减小--Concurrency参数），其理论值为：npuBlockNum * cacheBlockSize / (平均输入长度 + 平均输出长度)；若使用脚本发送请求，可适当提升脚本中设置的超时时间限制。

