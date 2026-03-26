# 重启服务器后，Docker服务启动失败

## 内核版本


## 问题现象
重启服务器后，执行restart docker命令报错，提示Failed to start Docker Application Container Engine。

## 问题根因
docker.service的启动配置错误，导致Docker服务启动失败。

## 解决方案
1. 执行命令 vi /usr/lib/systemd/system/docker.service 打开docker.service文件；2. 使用正确的ExecStart配置替换原有配置，包括指定graph路径、监听地址、日志选项等；3. 执行 systemctl daemon-reload 和 systemctl restart docker 重启Docker服务。

