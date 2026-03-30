# 部分OS安装完CANN后出现yum工具不可用的问题

## 内核版本


## 问题现象
在部分操作系统（如Euler 2.8和Kylin V10 SP1）上安装CANN后，执行yum命令报错：ModuleNotFoundError: No module named 'dnf'，导致yum工具无法使用。

## 问题根因
CANN安装过程中重新安装了Python并修改了环境变量，覆盖了系统自带的Python版本，而yum工具依赖系统默认的Python环境，因此无法正常运行。

## 解决方案
在用户主目录的.bashrc文件中注释掉新添加的Python环境变量，执行source ~/.bashrc使配置生效，并重新登录系统，即可恢复yum工具的正常使用。

