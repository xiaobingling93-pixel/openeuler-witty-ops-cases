# 安装鲲鹏DevKit失败的解决方法

## 内核版本


## 问题现象
安装DevKit失败，界面报错“Configure nginx Failed”，日志提示缺少依赖（如“C compiler /usr/bin/gcc is not found”）。即使安装缺失依赖后DevKit安装成功，网页仍无法访问。

## 问题根因
缺少必要的系统依赖导致安装失败；此外，在隔离网络环境下未配置代理，导致无法正常访问外网资源，进而影响WebUI的可用性。

## 解决方案
1. 根据tool_install.log日志提示，安装缺失的依赖（如gcc等）；2. 依赖安装完成后重新安装DevKit；3. 若处于隔离网络环境，需按照文档“隔离网络下配置代理”进行代理设置以确保WebUI可访问。

