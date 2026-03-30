# Fortran程序迁移至鲲鹏平台时提示Line truncated的解决方法

## 内核版本


## 问题现象
编译Fortran程序时出现错误：Error: Line truncated at (1) [-Werror=line-truncation]，具体发生在Projection_modul.f90文件第305行，该行代码长度超过132个字符。

## 问题根因
GFortran编译器在自由格式（free format）下默认限制每行代码不得超过132个字符，而原代码中某行长度超限，导致编译报错。不同编译器对此限制的处理方式可能存在差异。

## 解决方案
可通过以下任一方式解决：1）使用续行字符将超长行拆分为多行；2）在编译时添加选项 -ffree-line-length-none，取消对自由格式源码行长度的限制。

