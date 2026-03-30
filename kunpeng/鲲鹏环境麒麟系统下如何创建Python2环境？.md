# 鲲鹏环境麒麟系统下如何创建Python2环境？

## 内核版本


## 问题现象
因软件安装需求，需要在鲲鹏环境的麒麟系统下安装Python2环境。

## 问题根因


## 解决方案
1. 使用conda创建一个名为py27的新环境，并指定Python版本为2.7：`conda create -n py27 python2.7`；
2. 激活该环境：`conda activate py27`；
3. 验证Python版本：`python --version`；
4. 如需退出环境，执行：`conda deactivate`。

