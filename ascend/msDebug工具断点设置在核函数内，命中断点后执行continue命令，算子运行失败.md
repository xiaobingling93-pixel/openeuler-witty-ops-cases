# msDebug工具断点设置在核函数内，命中断点后执行continue命令，算子运行失败

## 内核版本


## 问题现象
使用msDebug工具在核函数内设置断点，命中断点后执行continue命令，算子运行失败，报错信息为'Synchronize stream failed. error code is 507035'，plog中显示aic error code=0x8000000000000000，且命中断点时通过ascend info cores命令观察到当前核的PC值与预期不符。

## 问题根因
kernel函数中workspace入参的空间大小在Tiling函数中被设置为0，导致经过单算子API调用后workspace地址变为非法。尽管该workspace在kernel函数中未被实际使用，但调试器在展示kernel入参时会对workspace指针进行解引用，从而引发算子运行错误。

## 解决方案
参考《CANN Ascend C 算子开发指南》中“工程化算子开发 > 算子实现 > Host侧tiling实现”章节，将WorkspaceSize从0设置为预留内存大小。具体做法是通过GetLibApiWorkSpaceSize接口获取API所需的workspace内存大小，并在Tiling函数中正确设置。示例代码：#include "tiling/platform/platform_ascendc.h"; auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo()); size_t systemWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize(); size_t* currentWorkspace = context->GetWorkspaceSizes(1); currentWorkspace[0] = systemWorkspaceSize;

