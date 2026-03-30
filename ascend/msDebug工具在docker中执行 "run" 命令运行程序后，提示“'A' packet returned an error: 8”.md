# msDebug工具在docker中执行 "run" 命令运行程序后，提示“'A' packet returned an error: 8”

## 内核版本


## 问题现象
在docker中使用msDebug工具执行 "run" 命令运行程序时，出现报错："'A' packet returned an error: 8"。

## 问题根因
该问题可能与“地址空间布局随机化”（ASLR）有关。

## 解决方案
在msDebug中执行命令：settings set target.disable-aslr false，以规避此问题。

