# 执行msprof命令未采集到AI Core Metrics数据

## 内核版本


## 问题现象
执行msprof命令后，屏幕显示性能解析数据，但无AI Core Metrics数据。查看$HOME/ascend/log/plog路径下Host侧日志信息，发现aclInit函数初始化日志异常。

## 问题根因
代码实现时，调用aclInit函数在aclrtSetDevice函数之后，导致Runtime无法下发AI Core性能数据采集开关任务，从而无法采集AI Core Metrics数据。

## 解决方案
调整代码顺序，确保aclInit函数在aclrtSetDevice函数之前最先调用，然后重新编译代码并执行Profiling。

