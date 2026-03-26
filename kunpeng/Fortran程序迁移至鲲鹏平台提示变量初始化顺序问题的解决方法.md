# Fortran程序迁移至鲲鹏平台提示变量初始化顺序问题的解决方法

## 内核版本


## 问题现象
编译时出现错误：'Symbol 'nx' is used before it is typed'，原因是REAL变量Q在声明时依赖INTEGER变量NX、NY、NZ，但这些整型变量的定义出现在Q之后，导致编译器无法识别。

## 问题根因
Fortran语言要求变量必须先声明后使用。在原代码中，数组Q的维度依赖于尚未声明的变量NX、NY、NZ，因此编译器报错。

## 解决方案
调整变量声明顺序，将INTEGER :: NX,NY,NZ放在REAL :: Q(...)之前，确保依赖的变量先被定义。

