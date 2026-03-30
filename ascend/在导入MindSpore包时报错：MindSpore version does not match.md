# 在导入MindSpore包时报错：MindSpore version does not match

## 内核版本


## 问题现象
在导入MindSpore包时出现错误提示：MindSpore version does not match。

## 问题根因
CANN包版本与MindSpore版本不兼容，可能由于安装了不兼容的CANN版本，或环境变量配置错误（例如系统中存在多个CANN版本，软链接指向了旧版本）。

## 解决方案
重新安装与MindSpore版本匹配的CANN run包，并执行安装目录下的set_env.sh脚本来正确配置环境变量。

