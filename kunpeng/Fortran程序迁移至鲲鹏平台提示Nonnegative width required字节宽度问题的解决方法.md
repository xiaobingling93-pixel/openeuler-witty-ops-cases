# Fortran程序迁移至鲲鹏平台提示Nonnegative width required字节宽度问题的解决方法

## 内核版本


## 问题现象
编译时出现错误：'Error: Nonnegative width required in format string at (1)'，具体出现在类似'READ(CTOKEN(1:NCHAR),'(I)') IDLIST'的语句中。

## 问题根因
标准Fortran要求在格式字符串中为整数输入指定非负的位宽（如I5），而Intel Fortran编译器支持不指定宽度的扩展语法（如I），但在GFortran（鲲鹏平台常用）中该写法不符合标准，因此报错。

## 解决方案
将格式字符串中的'(I)'修改为带有明确宽度的格式，例如'(I5)'，即把'READ(CTOKEN(1:NCHAR),'(I)') IDLIST'改为'READ(CTOKEN(1:NCHAR),'(I5)') IDLIST'。

