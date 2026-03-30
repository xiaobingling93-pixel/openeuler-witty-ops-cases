# 移植x86 xchgl汇编指令的方法

## 内核版本


## 问题现象
编译报错：{standard input}: Assembler messages: {standard input}:1222: Error: unknown mnemonic 'xchgl' -- 'xchgl x1,[x19,112]'。

## 问题根因
xchgl是x86上的汇编指令，用于交换寄存器/内存变量和寄存器的值，并在涉及内存变量时增加原子锁操作。该指令在鲲鹏（ARM架构）平台上不被支持。

## 解决方案
使用GCC提供的原子操作接口__atomic_exchange_n替换xchgl指令。例如，将内联汇编代码替换为：return __atomic_exchange_n(&_q_value, newValue, __ATOMIC_SEQ_CST); 其中第三个参数为内存屏障类型，建议在多线程临界区逻辑不清晰时使用__ATOMIC_SEQ_CST以确保一致性。

