# 未设置环境变量，导致ATC工具无法使用

## 内核版本


## 问题现象
输入模型转换的命令后，按回车提示 'bash: atc: command not found' 错误。

## 问题根因
ATC工具在CANN软件包中以二进制形式存在，使用前必须通过环境变量使能该二进制文件；未正确设置环境变量导致系统无法找到atc命令。

## 解决方案
在运行ATC工具前，需根据安装用户类型设置相应环境变量：若为root用户安装Ascend-cann-toolkit包，执行 '. /usr/local/Ascend/ascend-toolkit/set_env.sh'；若为非root用户，则执行 '. ${HOME}/Ascend/ascend-toolkit/set_env.sh'。若在非昇腾设备上安装开发套件包，还需额外设置LD_LIBRARY_PATH环境变量指向动态链接库路径。设置完成后，可通过 'atc --help' 验证工具是否可用。

