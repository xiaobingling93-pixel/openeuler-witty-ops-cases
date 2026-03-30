# MindSpore-server部署失败

## 内核版本


## 问题现象
在CentOS 7.6 (ARM)系统上，使用CANN 5.0.4、MindSpore 1.6.0、Python 3.7.5环境部署MindSpore-server 1.6.0时，启动服务器报错：AttributeError: module 'importlib' has no attribute 'util'。

## 问题根因
代码中使用了不正确的import语句'import importlib'，而实际应直接导入子模块'util'，即'import importlib.util'，导致在调用importlib.util时因模块未正确加载而报错。

## 解决方案
编辑文件/usr/local/python3.7.5/lib/python3.7/site-packages/mindspore_serving/server/worker/init_mindspore.py，将'import importlib'修改为'import importlib.util'。

