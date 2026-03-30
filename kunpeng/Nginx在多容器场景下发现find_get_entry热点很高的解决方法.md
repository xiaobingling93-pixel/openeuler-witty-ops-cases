# Nginx在多容器场景下发现find_get_entry热点很高的解决方法

## 内核版本


## 问题现象
Nginx在多容器场景下发现find_get_entry热点很高导致性能下降。

## 问题根因
容器基于镜像启动，所有的容器内的nginx访问的其实是镜像里的同一份nginx.cnf，所以会出现find_get_entry热点。

## 解决方案
进入每个容器，将nginx.cnf重命名，这样每个容器的配置文件就是独有的。具体步骤：1. 启动容器（docker start 容器名）；2. 进入容器并复制或重命名配置文件（例如使用 docker cp index.html 容器名:/usr/local/nginx/html/配置文件名）；3. 重新测试验证Nginx性能。

