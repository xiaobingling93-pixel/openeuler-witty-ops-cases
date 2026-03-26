# pip3安装软件包时，出现read time out报错

## 内核版本


## 问题现象
使用pip3下载相关依赖（如scipy）时出现read time out错误。

## 问题根因
网络不稳定导致下载时间过长、速度过慢，尤其在下载较大的包（如numpy和scipy）时，socket数据通信容易超时。

## 解决方案
更换为其他稳定的pip源，通过命令 'pip3 install <package> -i <source_url>' 指定可用的镜像源进行安装。

