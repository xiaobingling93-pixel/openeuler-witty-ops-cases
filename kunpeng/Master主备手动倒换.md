# Master主备手动倒换

## 内核版本


## 问题现象
集群运行过程中，进行主Master节点维护等动作时，需要手动进行主备倒换。Master主备倒换过程中Donau Scheduler存在不可服务时间，不可服务时间内执行CLI命令会显示异常。

## 问题根因


## 解决方案
方法一：重启主Master节点服务，促使服务在中断过程中切回备Master节点。操作步骤：1. 以DonauKit运维用户登录主Master节点；2. 切换至root账户；3. 执行 systemctl restart batch-master.service。方法二：配置Primary Master，使主Master恢复后自动切回。操作步骤：1. 以DonauKit运维用户登录目标Master节点；2. 切换至root账户；3. 编辑 /opt/batch/master/conf/master.properties 文件，设置 master.primary=true；4. 保存退出后执行 systemctl restart batch-master.service。详细说明可参考《HPC 22.0.RC1 用户指南》> 多瑙调度器 > 集群管理 > 高可用 > Master高可用章节。

