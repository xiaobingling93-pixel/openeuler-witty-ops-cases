# 编译Cufflinks时报GHash.hh:91:44: error错误

## 内核版本


## 问题现象
编译Cufflinks时报错，报错信息为：GHash.hh:91:44: error: type/value mismatch at argument 1 in template parameter list for ‘template<class _Tp> struct std::hash’
91 |     while (pos<fCapacity && hash[pos].hash<0) pos++;

## 问题根因
Cufflinks源码bug，已在最新master版本中修正。

## 解决方案
请下载最新的Cufflinks安装包。下载地址：https://codeload.github.com/cole-trapnell-lab/cufflinks/zip/master

