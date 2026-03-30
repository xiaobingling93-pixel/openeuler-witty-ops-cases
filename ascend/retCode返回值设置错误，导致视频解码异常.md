# retCode返回值设置错误，导致视频解码异常

## 内核版本


## 问题现象
调用aclvdecSendFrame接口发送一帧码流后，复用输出图片描述信息进行后续帧解码时，反复出现解码不成功或解码异常的情况。日志显示acldvppGetPicDescRetCode返回的retCode为2，表示解码失败。

## 问题根因
前一帧码流解码失败后，retCode被置为2，在复用输出图片描述信息时未重置该状态，导致后续帧解码时AscendCL仍读取到retCode为2，从而误判为解码失败。

## 解决方案
在复用输出图片描述信息前，需调用acldvppSetPicDescRetCode将retCode显式设置为0，以清除前一帧解码异常的状态，避免影响后续帧的解码判断。

