# 鲲鹏920 7260处理器是否支持svei8mm、svef32mm、 svef64mm、svebf16、i8mm、bf16 等相关指令集？

## 内核版本


## 问题现象
用户询问鲲鹏920 7260处理器是否支持svei8mm、svef32mm、svef64mm、svebf16、i8mm、bf16等相关指令集。

## 问题根因
鲲鹏920 7260处理器基于ARMv8架构，不支持SVE（Scalable Vector Extension）指令集，因此也不支持基于SVE的扩展指令如svei8mm、svef32mm、svef64mm、svebf16等。

## 解决方案
鲲鹏920 7260处理器不支持SVE指令集及其相关扩展指令。如需使用这些指令，需选择支持ARMv9或更高架构并明确支持SVE/SVE2的处理器。

