# 移植x86 bswap汇编指令的方法

## 内核版本


## 问题现象
编译报错：Error: unknown mnemonic 'bswap' -- 'bswap x3'。

## 问题根因
bswap是x86的字节序反序指令，在ARM64架构下不支持，需替换为ARM64的rev指令。

## 解决方案
将x86的bswap内联汇编代码替换为ARM64兼容的rev指令实现。具体地，原x86代码为：inline uint32_t bswap(uint32_t val) { __asm__("bswap %0" : "=r" (val) : "0" (val)); return val; }；在鲲鹏（ARM64）平台下应改为：static inline uint32_t bswap(uint32_t val) { __asm__("rev %w[dst], %w[src]" : [dst]"=r"(val) : [src]"r"(val)); return val; }。

