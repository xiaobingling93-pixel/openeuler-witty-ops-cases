# CentOS 7.6容器镜像内安装CANN包报错“which:command not found”

## 内核版本


## 问题现象
在CentOS 7.6容器镜像内安装CANN软件包时，报错“which:command not found”，导致安装中止。

## 问题根因
CANN软件包中部分组件依赖Linux工具which进行安装，但CentOS 7.6容器镜像默认未安装which命令。

## 解决方案
执行命令 `yum install -y which` 安装which工具，安装完成后继续执行CANN软件包的安装命令。

