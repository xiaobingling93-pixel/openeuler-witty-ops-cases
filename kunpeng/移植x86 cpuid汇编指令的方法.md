# 移植x86 cpuid汇编指令的方法

## 内核版本


## 问题现象
在鲲鹏平台上编译包含x86专有汇编指令'cpuid'的代码时，报错：/tmp/ccfaVZfw.s:34: Error: unknown mnemonic 'cpuid' -- 'cpuid'。

## 问题根因
cpuid是x86平台特有的汇编指令，用于获取CPU信息，而鲲鹏平台（ARM架构）不支持该指令。鲲鹏平台的CPU ID信息存储在midr_el1寄存器中，需通过读取该寄存器获取。

## 解决方案
将x86的cpuid汇编代码替换为ARM64读取midr_el1寄存器的代码。具体实现为：使用内联汇编"mrs %0, midr_el1"读取midr_el1寄存器值到变量s1中，并调整snprintf格式化输出。示例代码：
unsigned int s1 = 0;
unsigned int s2 = 0;
char cpu[32] = {0};
asm volatile
        (
         "mrs %0, midr_el1"
         : "=r"(s1)
         :
         :"memory" );
snprintf(cpu, sizeof(cpu), "%08X%08X", htonl(s1), htonl(s2));

