# 某Go程序迁移至鲲鹏服务器后异常结束问题的解决方法

## 内核版本


## 问题现象
基于Go语言开发的软件在迁移到鲲鹏服务器后进行测试时出现异常结束，报错信息包括 'unexpected fault address' 和 'signal SIGSEGV: segmentation violation code=0x32XXXX' 等。

## 问题根因
代码中使用了开源monkey补丁，在assembleJump函数中嵌入了针对x86架构的机器码（如 'mov rdx, main.b.f; jmp [rdx];'），该机器码在鲲鹏（ARM64）架构上不兼容。鲲鹏平台的mov指令一次只能处理16位立即数，而main.b.f是64位地址，直接使用x86汇编导致非法内存访问，从而引发段错误（SIGSEGV）。

## 解决方案
将x86架构下的汇编语句重构为适用于鲲鹏（ARM64）架构的汇编指令：使用 'mov x10, main.b.f; ldr x11, [x10]; br x11;' 实现相同功能，并将64位立即数分四次加载到寄存器中以适配鲲鹏指令集限制。修改后重新编译验证，问题解决。

