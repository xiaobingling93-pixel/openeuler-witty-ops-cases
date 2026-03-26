# 编译Cufflinks时报could not detect bam错误

## 内核版本


## 问题现象
编译Cufflinks时报错，报错信息为：“error: we could not detect bam”。

## 问题根因
configure文件中存在两处错误：一是判断设置错误，将succeeded变量设为no；二是指定通过<bam/version.hpp>来判断bam版本，而实际上bam的版本头文件名为version.h。

## 解决方案
修改configure文件：1. 将第5380行的“succeeded=no”改为“succeeded=yes”；2. 将“bam/version.hpp”替换为“bam/version.h”。修改后保存并重新编译即可。

