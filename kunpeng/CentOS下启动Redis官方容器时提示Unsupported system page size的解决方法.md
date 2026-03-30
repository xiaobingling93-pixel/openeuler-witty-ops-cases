# CentOS下启动Redis官方容器时提示Unsupported system page size的解决方法

## 内核版本


## 问题现象
在TaiShan服务器CentOS 7.6上使用docker run -it --rm redis命令启动Redis官方容器时，提示"<jemalloc>: Unsupported system page size"错误。

## 问题根因
Redis新版本默认使用jemalloc进行内存管理，而jemalloc在编译时就确定了page size大小。由于官方ARM镜像的编译环境的page size与当前运行环境的page size不一致，导致该问题。

## 解决方案
在运行环境下重新编译构建Redis镜像：1. 获取Redis官方镜像的Dockerfile（git clone https://github.com/docker-library/redis.git）；2. 进入对应版本目录（如5.0）；3. 执行docker build -t redis:5.0 . 构建镜像；4. 使用新构建的镜像运行容器（docker run -it --rm redis:5.0）即可成功启动。

