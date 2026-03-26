# pyACL推理提示acl.mdl.load_from_file failed，错误码145000

## 内核版本


## 问题现象
更换CANN版本后，使用pyACL进行推理时提示“acl.mdl.load_from_file failed”，错误码为145000。

## 问题根因
模型转换与模型执行时所使用的CANN版本不一致，导致模型文件与当前运行环境不兼容。

## 解决方案
方案一：在更换新的CANN版本后，重新将模型转换为OM格式；方案二：回退到原来的CANN版本，并重新执行推理。

