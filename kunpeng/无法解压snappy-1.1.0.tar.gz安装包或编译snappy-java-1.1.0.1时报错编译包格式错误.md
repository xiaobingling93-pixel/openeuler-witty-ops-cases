# 无法解压snappy-1.1.0.tar.gz安装包或编译snappy-java-1.1.0.1时报错编译包格式错误

## 内核版本


## 问题现象
执行编译时提示“gzip: stdin: not in gzip format”、“tar: Child returned status 1”、“tar: Error is not recoverable: exiting now”，表明下载的snappy压缩包格式错误或不完整，导致无法解压。

## 问题根因
Makefile中指定的Snappy压缩包下载地址（如http://snappy.googlecode.com/files/...）已失效或不可访问，导致自动下载的snappy-1.1.0.tar.gz文件内容不完整或非gzip格式，从而在解压时报错。

## 解决方案
1. 进入snappy-java-1.1.0.1/target目录，删除损坏的snappy-1.1.1.tar.gz文件；2. 编辑Makefile文件，注释掉原有的curl下载命令；3. 手动使用wget从有效地址（如http://src.fedoraproject.org/repo/pkgs/snappy/snappy-1.1.0.tar.gz/c8f3ef29b5281e78f4946b2d739cea4f/snappy-1.1.0.tar.gz）下载正确的snappy-1.1.0.tar.gz包，并确保其完整性。

