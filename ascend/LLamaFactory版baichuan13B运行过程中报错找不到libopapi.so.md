# LLamaFactory版baichuan13B运行过程中报错找不到libopapi.so

## 内核版本


## 问题现象
LLamaFactory版baichuan13B运行过程中报错找不到libopapi.so，屏显报错提示为“RuntimeError: aclnnForeachMulScalarInplace or aclnnForeachMulScalarInplaceGetWorkspaceSize not in libopapi.so, or libopapi.so not found.”

## 问题根因
系统无法找到libopapi.so动态库文件，导致相关算子调用失败。

## 解决方案
执行命令：export LD_PRELOAD=/usr/local/Ascend/ascend-toolkit/latest/lib64/libopapi.so:$LD_PRELOAD，将libopapi.so加入预加载库路径。

