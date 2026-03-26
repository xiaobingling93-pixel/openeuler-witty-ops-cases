# 如何重新解析TEXT格式的Profiling文件

## 内核版本


## 问题现象
在同一版本的MindStudio Insight软件下，再次导入TEXT格式的Profiling文件时，不会重新解析数据。

## 问题根因
系统缓存了之前的解析结果（存储在mindstudio_insight_data.db文件中），导致重复导入时跳过重新解析。

## 解决方案
删除profiling数据目录中的解析结果文件mindstudio_insight_data.db后，再次导入数据即可重新解析。

