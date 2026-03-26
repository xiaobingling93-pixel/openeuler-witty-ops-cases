# FDS运行时错误

## 内核版本


## 问题现象
FDS运行时出现错误，报错信息为：“Fortran runtime error: Cannot open file 'weak_scaling_test_128_0022_04.s3d': Too many open files”，表明系统打开的文件数超过限制。

## 问题根因
FDS在运行过程中需要读写大量文件，而系统默认的最大同时打开文件数限制（通常为1024）不足以满足其需求，导致“Too many open files”错误。

## 解决方案
通过执行命令“ulimit -n 10240”提高系统允许同时打开的最大文件数。Taishan服务器支持同时打开上千万个文件，可根据实际需求调整该限制。

