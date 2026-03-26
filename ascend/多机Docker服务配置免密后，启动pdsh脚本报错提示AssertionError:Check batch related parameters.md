# 多机Docker服务配置免密后，启动pdsh脚本报错提示AssertionError:Check batch related parameters

## 内核版本


## 问题现象
多机Docker服务配置免密后，启动pdsh脚本报错提示AssertionError:Check batch related parameters。

## 问题根因
启动节点的megatron_config.json文件未同步到其他节点上。

## 解决方案
执行scp命令将启动节点的megatron_config.json文件同步到其他节点的相同目录下，例如：scp /home/GPT-NeoX/megatron_config.json root@ip2:/soft/GPT-NeoX/，并依次对其他节点执行类似操作。

