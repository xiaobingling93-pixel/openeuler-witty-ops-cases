# 替换x86 rdtsc汇编指令

## 内核版本


## 问题现象
在鲲鹏平台编译包含x86 rdtsc汇编指令的代码时，报错：error: impossible constraint in ‘asm’，具体代码为：__asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));。

## 问题根因
rdtsc是x86平台特有的指令，用于读取时间戳计数器（TSC），而鲲鹏（ARM64）平台不支持该指令，需使用平台等效方法替代。

## 解决方案
提供两种替代方案：方法一，使用Linux系统调用clock_gettime(CLOCK_MONOTONIC, &tmp)近似模拟，根据服务器主频换算时间值；方法二，启用ARM64性能监控寄存器PMCCNTR_EL0，通过内核模块（如GitHub项目armv8_pmu_cycle_counter_el0）使能用户态访问，并使用内联汇编 asm volatile("mrs %0, pmccntr_el0" : "=r"(val)) 读取计数器值。

