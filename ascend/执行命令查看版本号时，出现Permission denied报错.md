# 执行命令查看版本号时，出现Permission denied报错

## 内核版本


## 问题现象
使用命令 ./Ascend-mindxsdk-mxvision_{version}_linux-{arch}.run --version 查看版本号时，出现类似 'rm: cannot remove "xxx": Permission denied' 的错误提示。

## 问题根因
安装过其他未正确安装的软件包，该软件包在“/tmp”路径下留有缓存，影响到当前版本的执行。

## 解决方案
可执行以下命令解决：sudo rm -rf /tmp/mxVision；如果无sudo权限，可执行：chmod u+w -R /tmp/mxVision && rm -rf /tmp/mxVision。其中路径“/tmp/mxVision”需根据实际情况替换。

