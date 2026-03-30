# 使用Debian10操作系统，安装时报错：File docker.service does not exist或Docker.service failed because the control procexx exited

## 内核版本


## 问题现象
使用MindCluster Ascend Deployer工具在Debian10操作系统上安装软件包时，报错提示：file docker.service does not exist 或 docker.service failed because the control process exited。

## 问题根因
docker安装过程中异常终止，导致系统中存在不完整的安装残留，使得后续安装流程无法正确识别或启动docker服务。

## 解决方案
1. 执行 which docker 命令查看当前docker二进制文件路径（例如 /usr/bin/docker）；2. 将该路径下的docker二进制文件重命名备份（如 mv /usr/bin/docker /usr/bin/docker.bak）；3. 重新执行Ascend Deployer的安装步骤，以触发docker的完整重新安装。

