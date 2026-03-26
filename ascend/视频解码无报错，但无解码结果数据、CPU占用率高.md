# 视频解码无报错，但无解码结果数据、CPU占用率高

## 内核版本


## 问题现象
应用日志中无ERROR报错，但没有解码结果数据输出；同时在运行应用程序的Linux服务器上执行top命令，发现该应用进程的CPU占用率持续升高。

## 问题根因
未正确调用aclvdecSetChannelDescThreadId接口绑定用户创建的线程，导致aclrtProcessReport接口调用失败（返回错误码107012，表示线程未订阅或重复订阅），从而无法触发回调函数获取解码结果数据，造成CPU持续空转占用率升高。

## 解决方案
按照VDEC视频解码接口调用流程，确保：1）创建新线程并在其线程函数中调用aclrtProcessReport接口；2）调用aclvdecSetChannelDescThreadId接口将该线程与解码通道绑定；3）资源释放时按顺序销毁通道、通道描述信息后再销毁线程。参考官方文档或VDEC功能样例代码进行修正。

