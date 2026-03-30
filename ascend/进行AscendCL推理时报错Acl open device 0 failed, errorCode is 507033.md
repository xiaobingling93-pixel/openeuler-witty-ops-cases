# 进行AscendCL推理时报错Acl open device 0 failed, errorCode is 507033

## 内核版本


## 问题现象
通过C++ AscendCL接口编写的yolov7MultiInput demo在运行时调用aclrtSetDevice()接口返回错误码507033。

## 问题根因
环境变量未正确配置，缺少运行时所需的链接库文件，导致无法正常调用Device相关功能。

## 解决方案
在~/.bashrc中添加运行时链接库路径：export LD_LIBRARY_PATH=${THIRDPART_PATH}/lib:$LD_LIBRARY_PATH，并执行source ~/.bashrc使配置生效。

