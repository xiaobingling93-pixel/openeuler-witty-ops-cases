# ATC模型转换报错：'sys' has no attibute 'argv'

## 内核版本


## 问题现象
执行ATC模型转换时，报错提示：module 'sys' has no attribute 'argv'。

## 问题根因
Python未安装或Python环境异常，导致sys模块缺少argv属性。

## 解决方案
参考《CANN软件安装指南》中“安装开发环境 > 安装依赖”章节，正确安装Python并配置环境变量。

