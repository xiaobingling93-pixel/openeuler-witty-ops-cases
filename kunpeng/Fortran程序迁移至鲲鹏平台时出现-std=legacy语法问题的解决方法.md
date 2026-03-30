# Fortran程序迁移至鲲鹏平台时出现-std=legacy语法问题的解决方法

## 内核版本


## 问题现象
编译报错：Error: Actual argument contains too few elements for dummy argument ‘wgrd’ (1/4) at (1)，具体发生在调用subroutine get_ij时，传入参数数量与接口定义不一致。

## 问题根因
GFortran默认使用较新的Fortran标准（如F95、F2003等），对语法要求更严格，而旧代码遵循的是较宽松的F77规范，导致在新标准下因参数数量不匹配而报错。

## 解决方案
使用-std=legacy编译选项，使编译器遵循旧的F77语法规范，从而避免因参数数量不一致导致的编译错误。

