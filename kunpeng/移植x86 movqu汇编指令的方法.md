# 移植x86 movqu汇编指令的方法

## 内核版本


## 问题现象
编译报错：unknown mnemonic 'movqu' -- 'movqu'。

## 问题根因
movqu为x86指令集中的指令，在鲲鹏（ARM架构）平台上无法使用。该指令用于实现寄存器到寄存器、寄存器到内存地址的128位数据拷贝。

## 解决方案
针对x86的movqu指令在鲲鹏平台上的替代方案：第一种用法（从内存或寄存器加载数据到xmm寄存器）可使用ARM NEON的ld1指令替代，例如 'ld1 {v0.16b}, [%[a]], #16'；第二种用法（从xmm寄存器存储数据到内存或另一寄存器）可使用st1指令替代，例如 'st1 {v0.16b}, [%[result]], #16'。具体示例见原文代码对比。参考文档：https://c9x.me/x86/html/file_module_x86_id_184.html 和 http://infocenter.arm.com/help/topic/com.arm.doc.dui0802a/DUI0802A_armasm_reference_guide.pdf。

