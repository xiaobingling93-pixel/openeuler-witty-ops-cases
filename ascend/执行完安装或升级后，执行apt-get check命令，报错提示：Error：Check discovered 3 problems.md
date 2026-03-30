# 执行完安装或升级后，执行apt-get check命令，报错提示：Error：Check discovered 3 problems

## 内核版本


## 问题现象
使用MindCluster Ascend Deployer工具执行完安装或升级后，执行apt-get check或yum check命令，报错提示：Error：Check discovered 3 problems或The following packages have unmet dependencies：Depends: gcc-11（=11.2.0-19ubuntu1）but 11.4.0-1ubuntu1~22.04 is to be installed。

## 问题根因
已安装的软件包存在不同的依赖，且这些依赖关系存在冲突。

## 解决方案
请勿执行fix_broken类操作，联系华为技术支持定位解决依赖冲突。

