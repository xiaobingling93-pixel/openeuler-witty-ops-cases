# 在调用torch时遇到报错“ModuleNotFoundError: No module named 'torch._C'”

## 内核版本


## 问题现象
在调用torch时出现错误：ModuleNotFoundError: No module named 'torch._C'。报错发生在.../code/pytorch/torch/__init__.py，表明系统试图从当前目录下的torch文件夹导入模块，但该目录下缺少必要的编译模块torch._C。

## 问题根因
当前工作目录为.../code/pytorch，在执行import torch时，Python优先从当前目录查找torch包，而该目录下的torch并非通过pip或conda安装的完整PyTorch包，缺少编译后的torch._C模块，导致导入失败。

## 解决方案
应确保导入的是系统环境中已正确安装的PyTorch包，而非当前目录下的torch源码目录。解决方法是切换到其他非PyTorch源码目录下执行脚本，避免Python将本地torch目录误认为是安装包。

