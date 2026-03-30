# msprof解析后，输出文件异常，缺少modelid或iterid

## 内核版本


## 问题现象
使用CANN 6.3.RC2对Profiling数据进行解析后，升级至CANN 7.0.0，使用msprof导出的summary文件数据量过大，且文件名缺失modelid或iterid。

## 问题根因
CANN解析后会导出sqlite文件，在升级CANN版本后，如果直接执行msprof export命令，会复用旧版本生成的sqlite文件，从而导致导出的profile文件异常。

## 解决方案
1. 删除log、sqlite、summary文件夹；2. 执行命令行msprof --parse=on --output=xxx；3. 再执行msprof --export=on --iteration-id=xx --model-id=xx --output=xxx，重新导出summary文件。

