# COSBench读取大文件失败的解决方法

## 内核版本


## 问题现象
当测试256k get时，COSBench读取文件失败，日志中出现错误信息：'Uploading large file fails with ResetException: Failed to reset the request input stream'。

## 问题根因
COSBench默认读文件的缓冲区大小是128k，当测试的文件大小超过该值（如256k）时，会导致读取失败。

## 解决方案
在/path/to/cosbench/cosbench-start.sh脚本的Java命令行中添加参数：-Dcom.amazonaws.sdk.s3.defaultStreamBufferSize=<YOUR_MAX_PUT_SIZE>，以增大默认流缓冲区大小，适应更大的文件读取需求。

