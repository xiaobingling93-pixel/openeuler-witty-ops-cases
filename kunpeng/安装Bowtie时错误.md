# 安装Bowtie时错误

## 内核版本


## 问题现象
安装Bowtie时执行make编译报错，具体错误信息为：narrowing conversion of ‘-1’ from ‘int’ to ‘char’ inside { } [-Wnarrowing]。

## 问题根因
代码中存在缩窄转换错误，即将整型常量-1隐式转换为char类型时，由于char在某些平台（如ARM）上默认为unsigned char，导致无法表示负值，从而触发编译错误。

## 解决方案
修改Bowtie源码中的alphabet.cpp文件，将第276行的数组定义从'char mask2iupac[16] = {...}'改为'signed char mask2iupac[16] = {...}'，以显式指定使用有符号字符类型，避免缩窄转换错误。

