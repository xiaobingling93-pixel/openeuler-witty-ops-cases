# ST配置界面报错：Credentials of toolchain must be the same as CANN machine

## 内核版本


## 问题现象
运行算子ST测试时，MindStudio配置界面显示错误信息：Error: Credentials of toolchain must be the same as CANN machine。

## 问题根因
远程执行ST测试所使用的CANN软件包与当前工程配置的CANN软件包不一致。

## 解决方案
重新配置远程CANN软件包地址，并重启MindStudio。

