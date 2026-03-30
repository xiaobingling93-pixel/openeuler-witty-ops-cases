# 编译MiniDFT时报错

## 内核版本


## 问题现象
编译MiniDFT时报错，报错信息为：“pwscf.f90:(.text+0x20): undefined reference to `dfftw_init_threads”。

## 问题根因
fftw没有threads模块。

## 解决方案
重新编译fftw，编译时添加--enable-threads参数。

