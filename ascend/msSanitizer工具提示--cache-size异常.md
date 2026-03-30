# msSanitizer工具提示--cache-size异常

## 内核版本


## 问题现象
使用msSanitizer工具进行异常检测时，提示"113023 records undetected, please use --cache-size=xx to run the operator again"。

## 问题根因
算子执行信息的大小超过工具默认分配GM内存的大小，导致部分信息丢失。

## 解决方案
根据提示修改--cache-size值，并重新运行算子进行异常检测。

