# 替换x86 pand汇编指令

## 内核版本


## 问题现象
编译报错：unknown mnemonic 'pand' -- 'pand'。

## 问题根因
pand是x86指令集中的指令，无法在鲲鹏设备（ARM架构）上使用。其功能是对寄存器或内存中的128位（xmm）或64位（mm）数据进行按位与运算。

## 解决方案
在鲲鹏平台上使用ARM NEON指令AND替代。对于128位数据使用AND Vd.16b, Vn.16b, Vm.16b，对于64位数据使用AND Vd.8b, Vn.8b, Vm.8b。示例代码展示了如何通过内联汇编加载两个数组、执行按位与并存储结果。参考ARM指令手册：http://infocenter.arm.com/help/topic/com.arm.doc.dui0802a/DUI0802A_armasm_reference_guide.pdf

