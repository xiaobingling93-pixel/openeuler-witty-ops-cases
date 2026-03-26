# 移植x86 cmpxchgl汇编指令的方法

## 内核版本


## 问题现象
编译报错：{standard input}: Assembler messages: {standard input}:1222: Error: unknown mnemonic 'cmpxchgl '。

## 问题根因
cmpxchgl是x86上的汇编指令，用于比较并交换操作数，而鲲鹏架构上没有对应的指令。

## 解决方案
使用GCC的原子操作接口__atomic_compare_exchange_n进行替换。例如，将原有的内联汇编代码替换为：return __atomic_compare_exchange_n(&m_value, &expectedValue, newValue, false, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);

