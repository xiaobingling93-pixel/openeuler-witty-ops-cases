# 移植atomic64_add_and_return原子操作函数的方法

## 内核版本


## 问题现象
在将代码从x86架构移植到鲲鹏平台时，原有的基于x86汇编实现的atomic64_add_and_return原子操作函数无法直接使用，需要适配ARM64架构。

## 问题根因
x86架构使用lock前缀和xaddq指令实现原子加并返回操作，而鲲鹏（ARM64）平台不支持该汇编指令，需采用平台兼容的实现方式。

## 解决方案
在鲲鹏平台下，使用GCC内置的原子操作函数__sync_add_and_fetch替代原有的嵌入式汇编实现。具体代码为：static __inline__ long atomic64_add_and_return(long i, atomic64_t *v) { return __sync_add_and_fetch(&((v)->counter), i); }

