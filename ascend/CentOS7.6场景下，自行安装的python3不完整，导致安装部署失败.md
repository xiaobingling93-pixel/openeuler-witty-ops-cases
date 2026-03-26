# CentOS7.6场景下，自行安装的python3不完整，导致安装部署失败

## 内核版本


## 问题现象
在CentOS7.6系统中，使用自行安装的python3执行MindCluster Ascend Deployer工具进行安装部署时失败。

## 问题根因
用户在CentOS7.6_aarch64操作系统下自行安装的python3功能不完整，缺少libselinux依赖库，而Ascend Deployer工具优先使用该python3环境，从而导致安装失败。

## 解决方案
重新安装libselinux依赖包，然后再次执行MindCluster Ascend Deployer的安装命令，即可成功完成安装。

