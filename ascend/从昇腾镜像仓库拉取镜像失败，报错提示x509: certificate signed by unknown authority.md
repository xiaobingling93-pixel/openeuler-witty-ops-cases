# 从昇腾镜像仓库拉取镜像失败，报错提示x509: certificate signed by unknown authority

## 内核版本


## 问题现象
从昇腾镜像仓库（ascendhub.huawei.com）拉取镜像时失败，系统报错：x509: certificate signed by unknown authority。

## 问题根因
Docker未配置insecure-registries，导致无法信任昇腾镜像仓库的SSL证书。

## 解决方案
1. 检查是否已配置Docker代理；2. 如需代理，创建并配置/etc/systemd/system/docker.service.d/http-proxy.conf文件；3. 编辑/etc/docker/daemon.json文件，添加"insecure-registries": ["ascendhub.huawei.com"]；4. 执行systemctl daemon-reload和systemctl restart docker命令重启Docker服务。

