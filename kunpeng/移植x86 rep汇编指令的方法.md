# 移植x86 rep汇编指令的方法

## 内核版本


## 问题现象
编译报错：unknown mnemonic 'rep' -- 'rep'。

## 问题根因
rep为x86的重复执行指令，在ARM64架构下不支持，需替换为ARM64的.rept指令。

## 解决方案
将x86的'rep;nop'汇编指令替换为ARM64兼容的实现方式，例如：
#define __nops(n) ".rept " #n "\nnop\n.endr\n"
#define nops(n) asm volatile(__nops(n))

