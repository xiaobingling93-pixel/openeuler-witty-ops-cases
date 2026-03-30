# Fortran程序迁移至鲲鹏平台时出现逻辑变量判断问题的解决方法

## 内核版本


## 问题现象
编译时出现错误：'Logicals at (1) must be compared with .eqv. instead of =='，具体代码行为 'WANTSQRTS = (FSCOP == .TRUE.)'。

## 问题根因
标准Fortran要求逻辑变量的相等性比较应使用.eqv.操作符，而Intel编译器支持使用==的非标准扩展写法，在迁移到鲲鹏平台（使用符合标准的编译器）时该写法不被支持，导致编译报错。

## 解决方案
将逻辑比较语句中的'=='替换为标准Fortran操作符'.eqv.'，即将 'WANTSQRTS = (FSCOP == .TRUE.)' 修改为 'WANTSQRTS = (FSCOP .eqv. .TRUE.)'。

