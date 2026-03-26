# 编译CNVnator时报[cnvnator] Error 1错误

## 内核版本


## 问题现象
编译CNVnator时出现链接错误，报错信息为：/usr/bin/ld: samtools/htslib-1.9/libhts.a(hfile_s3.o): undefined reference to symbol 'HMAC@@libcrypto.so.10'，以及 /usr/lib64/libcrypto.so.10: error adding symbols: DSO missing from command line，最终导致 make: *** [cnvnator] Error 1。

## 问题根因
编译链接过程中缺少对 libcrypto 库的显式链接，导致链接器无法解析 HMAC 符号引用。

## 解决方案
执行 make 命令时添加 LIBS 参数以显式链接 libcrypto 库，具体命令为：make LIBS="-lcrypto"。

