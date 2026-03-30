# 运行“Run tests sequebtially”时卡死

## 内核版本


## 问题现象
运行“Run tests sequebtially”时，执行至asyncio卡死。

## 问题根因
编译安装自带测试集的Python3版本（如Python3.6.0），造成执行至asyncio卡死。

## 解决方案
方式一：移除configure步骤中的优化参数，编译时不进行测试集校验。方式二：移除编译目录Lib/test/内asyncio相关的测试脚本。

