# 部署Service服务时出现LLMPythonModel initializes fail的报错提示

## 内核版本


## 问题现象
部署Service服务时，出现LLMPythonModel initializes fail的报错。

## 问题根因
ibis缺少Python依赖。

## 解决方案
进入Service安装路径下的logs目录，打开Python日志，根据日志报错信息，安装需要的依赖。

