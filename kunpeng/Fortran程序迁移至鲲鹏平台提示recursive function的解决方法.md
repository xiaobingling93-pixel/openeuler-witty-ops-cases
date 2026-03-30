# Fortran程序迁移至鲲鹏平台提示recursive function的解决方法

## 内核版本


## 问题现象
在将Fortran程序迁移至鲲鹏平台时，编译报错：'func' is the name of a recursive function and so refers to the result variable. Use an explicit RESULT variable for direct recursion。错误发生在递归函数中直接使用函数名作为返回值的场景。

## 问题根因
Fortran语言规范要求递归函数（recursive function）必须使用RESULT关键字显式声明返回值变量，而不能直接使用函数名作为返回值。Intel Fortran编译器（ifort）支持非标准的函数名作为返回值的写法，但鲲鹏平台使用的编译器（如GCC/gfortran）遵循标准规范，因此报错。

## 解决方案
在递归函数定义中添加RESULT关键字，显式指定返回值变量。例如将 'recursive Function func(n)' 修改为 'recursive Function func(n) result(r)'，并在函数体内使用'r'代替'func'作为返回值变量。

