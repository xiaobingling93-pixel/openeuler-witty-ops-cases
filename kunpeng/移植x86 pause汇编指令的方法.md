# 移植x86 pause汇编指令的方法

## 内核版本


## 问题现象
编译报错：Error: unknown mnemonic 'pause' -- 'pause'。

## 问题根因
pause指令是x86平台特有的汇编指令，用于提高spin-wait循环的性能，在鲲鹏（ARM架构）平台上不被支持，需替换为ARM平台对应的yield指令。

## 解决方案
将x86平台的内联汇编代码 __asm__ __volatile__("pause" : : : "memory"); 替换为鲲鹏平台支持的 __asm__ __volatile__("yield" : : : "memory");。

