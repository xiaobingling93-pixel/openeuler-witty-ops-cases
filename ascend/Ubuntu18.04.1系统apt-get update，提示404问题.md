# Ubuntu18.04.1系统apt-get update，提示404问题

## 内核版本


## 问题现象
在Ubuntu 18.04.1系统中执行apt-get update命令时，返回404错误。

## 问题根因
系统为ARM架构，但配置的APT源为x86架构的Ubuntu源，导致无法找到对应架构的软件包，从而报404错误。

## 解决方案
将APT源地址中的'ubuntu'替换为'ubuntu-ports'，使用适用于ARM架构的源。例如：deb http://mirrors.aliyun.com/ubuntu-ports/ bionic main restricted universe multiverse，并更新所有相关源条目后重新执行apt-get update命令。

