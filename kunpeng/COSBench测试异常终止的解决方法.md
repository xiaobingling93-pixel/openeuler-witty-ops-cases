# COSBench测试异常终止的解决方法

## 内核版本


## 问题现象
COSBench校验数据完整性失败导致测试终止，具体表现为日志中出现错误：'Unable to verify integrity of data download. Client calculated content hash didn't match hash calculated by Amazon S3. The data may be corrupt.'

## 问题根因
COSBench在执行过程中对从S3兼容存储下载的数据进行MD5校验失败，导致测试流程异常终止。

## 解决方案
在COSBench启动脚本 /path/to/cosbench/cosbench-start.sh 的java命令行中添加参数 '-Dcom.amazonaws.services.s3.disableGetObjectMD5Validation=true' 以关闭MD5校验，然后重启所有COSBench进程。

