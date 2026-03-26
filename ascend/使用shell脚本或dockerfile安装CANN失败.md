# 使用shell脚本或dockerfile安装CANN失败

## 内核版本


## 问题现象
安装CANN包时弹出人机交互需要手动同意EULA协议，导致安装脚本无法顺利执行。

## 问题根因
CANN安装脚本默认需要用户手动确认EULA协议，而在非交互式环境（如shell脚本或Dockerfile）中无法完成该交互，导致安装中断。

## 解决方案
在安装CANN软件包的命令中添加参数以自动同意协议，例如：echo y | ./Ascend-cann-toolkit_****.run --install 或 ./Ascend-cann-toolkit_****.run --install --quiet。

