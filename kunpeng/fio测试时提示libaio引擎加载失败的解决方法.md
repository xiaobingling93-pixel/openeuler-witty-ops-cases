# fio测试时提示libaio引擎加载失败的解决方法

## 内核版本


## 问题现象
执行fio测试时，提示libaio引擎加载失败。

## 问题根因
客户端所安装的fio版本不支持libaio引擎。

## 解决方案
安装libaio-devel，重新编译安装fio。具体操作如下：1. 用yum安装libaio-devel依赖包：yum -y install libaio-devel；2. 进入到fio源码目录：cd /path/to/fio/；3. 配置编译选项：./configure；4. 编译：make；5. 安装：make install。

