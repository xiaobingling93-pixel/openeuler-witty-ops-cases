# 通过导入基础镜像的方式安装MEF Center失败

## 内核版本


## 问题现象
用户通过docker load命令导入本地的Ubuntu:22.04基础镜像的方式安装MEF Center失败。

## 问题根因
当MEF Center安装环境的Docker版本为23.0及以上时，默认启用BuildKit作为镜像构建工具，并尝试从镜像仓库重新获取依赖的基础镜像。若环境配置的镜像仓或Docker公共镜像仓不可用，且基础镜像仅通过离线方式导入，则会导致MEF Center组件镜像构建失败，从而造成安装失败。

## 解决方案
在安装MEF Center前，执行命令 export DOCKER_BUILDKIT=0 以关闭Docker的BuildKit功能。

