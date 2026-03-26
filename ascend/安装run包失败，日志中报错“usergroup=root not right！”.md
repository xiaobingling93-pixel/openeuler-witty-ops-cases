# 安装run包失败，日志中报错“usergroup=root not right！”

## 内核版本


## 问题现象
安装run包失败，日志中报错“usergroup=root not right！”。

## 问题根因
使用非root用户登录环境，切换至root用户执行安装操作时，切换后系统环境变量USER值仍为登录环境的非root用户。

## 解决方案
执行命令 export USER=root 手动将USER环境变量设置为实际执行安装的用户后，再进行安装。

