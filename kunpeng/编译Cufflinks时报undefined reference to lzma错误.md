# 编译Cufflinks时报undefined reference to lzma错误

## 内核版本


## 问题现象
编译Cufflinks时报错，报错信息为：“undefined reference to 'lzma_stream_buffer_bound'”。

## 问题根因
没有安装lzma相关依赖包。

## 解决方案
执行以下命令安装xz-devel.aarch64：yum install xz-devel.aarch64

