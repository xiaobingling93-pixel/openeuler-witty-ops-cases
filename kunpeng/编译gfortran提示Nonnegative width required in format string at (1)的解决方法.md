# 编译gfortran提示Nonnegative width required in format string at (1)的解决方法

## 内核版本


## 问题现象
通过gfortran对Makefile执行make编译时报“Error: Nonnegative width required in format string at (1)”错误，具体报错示例为：test_MyFile.f:1156:51: read( Test_OutputParamterVal(test_para, '(I)') Error: Nonnegative width required in format string at (1)

## 问题根因
在Fortran格式化字符串中使用了未指定非负位宽的格式符（如'I'），而gfortran要求整数格式符必须明确指定非负宽度。

## 解决方案
修改源文件test_MyFile.f，将格式字符串'(I)'改为带有明确宽度的格式如'(I5)'，例如：将read( Test_OutputParamterVal(test_para, '(I)')修改为read( Test_OutputParamterVal(test_para, '(I5)')，然后重新执行make即可正常编译通过。

