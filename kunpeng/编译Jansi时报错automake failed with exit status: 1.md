# 编译Jansi时报错automake failed with exit status: 1

## 内核版本


## 问题现象
编译Jansi时提示以下错误信息：
[INFO] /usr/share/automake-1.13/am/ltlibrary.am: warning: 'libjansi.la': linking libtool libraries using a non-POSIX
[INFO] /usr/share/automake-1.13/am/ltlibrary.am: archiver requires 'AM_PROG_AR' in 'configure.ac'
[INFO] Makefile.am:20:   while processing Libtool library 'libjansi.la'
[INFO] autoreconf: automake failed with exit status: 1

## 问题根因
configure.ac 文件中缺少 AM_PROG_AR 宏定义，导致在使用非 POSIX 兼容的归档器链接 libtool 库时 automake 失败。

## 解决方案
在编译的库目录下找到 configure.ac 文件，用文本编辑器打开，在文件末尾添加 AM_PROG_AR 宏。例如：
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LIBTOOL([disable-static])
AM_PROG_AR

