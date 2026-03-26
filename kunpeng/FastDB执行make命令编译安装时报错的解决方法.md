# FastDB执行make命令编译安装时报错的解决方法

## 内核版本


## 问题现象
FastDB执行make命令编译安装时提示“error: call of overloaded ‘fmax(float&, float&)’ is ambiguous quote.high = fmax(quote.open, quote.close);”和“error: call of overloaded ‘fmin(float&, float&)’ is ambiguous quote.low = fmin(quote.open, quote.close);”。

## 问题根因
testtimeseries.cpp文件中的fmax函数和fmin函数与cmath头文件中定义的同名函数冲突，导致函数调用存在歧义。

## 解决方案
1. 打开examples/testtimeseries.cpp文件；2. 将文件中所有fmax替换为fmax_t，所有fmin替换为fmin_t（例如使用vim命令：:%s/fmax/fmax_t/g 和 :%s/fmin/fmin_t/g）；3. 保存并退出；4. 重新执行make命令进行编译。

