# Device芯片登录Authentication failed,Connection refused问题

## 内核版本


## 问题现象
在尝试通过SSH登录Device芯片时，出现两种问题：一是输入密码始终提示错误（Authentication failed），初步判断为Device端芯片密码被修改且无法找回；二是提示'Connection refused'，即无法连接到目标主机的22端口。

## 问题根因
问题一的根本原因是Device芯片的默认密码已被修改，而带外复位、带内复位或重装驱动均无法恢复密码；问题二的根本原因是Device芯片上的SSH服务未启用，导致连接被拒绝。

## 解决方案
针对问题一，需通过重装固件并使用--full –reset参数来恢复初始化密码，之后使用默认用户名HwHiAiUser和初始密码Huawei2012#登录。针对问题二，首先使用npu-smi info -l查看NPU ID，然后执行npu-smi set -t ssh-enable -i <ID> -d 1启用SSH服务，接着执行热复位命令npu-smi set -t reset -i <ID> -c 0 -m 1，最后即可通过SSH正常登录Device芯片。

