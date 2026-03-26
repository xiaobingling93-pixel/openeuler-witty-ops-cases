# 编译Cufflinks时报could not find htslib错误

## 内核版本


## 问题现象
编译Cufflinks时，make提示找不到htslib。

## 问题根因
使用了samtools内置的htslib，但当前版本的Cufflinks不支持该内置版本。

## 解决方案
需要独立安装htslib，将生成的libhts.*复制到系统库路径中。具体步骤为：tar -xvf htslib-1.9.tar.bz2；cd htslib-1.9；make；cp libhts.* /usr/local/lib。

