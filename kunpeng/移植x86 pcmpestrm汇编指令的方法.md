# 移植x86 pcmpestrm汇编指令的方法

## 内核版本


## 问题现象
编译报错Error: unknown mnemonic 'pcmpestrm' -- 'pcmpestrm'。

## 问题根因
pcmpestrm指令是x86指令集中SSE4.2的专用指令，用于高效字符串比较，而鲲鹏（ARM架构）平台不支持该x86特定指令，因此在编译时无法识别该汇编指令导致报错。

## 解决方案
根据实际使用模式（PCMPSTR_EQUAL_ANY | PCMPSTR_UBYTE_OPS），使用C语言结合ARM NEON数据类型重新实现该指令的功能。具体方法是将输入的128位寄存器数据转换为字节数组，通过双重循环逐字节比较str2中每个字符是否在str1中出现，并将匹配结果按位设置到16位返回值中。示例代码使用__oword联合体对齐数据，并用位运算构建结果，替代原x86内联汇编实现。

