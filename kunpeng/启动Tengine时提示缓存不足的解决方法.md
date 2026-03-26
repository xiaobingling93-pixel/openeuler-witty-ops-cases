# 启动Tengine时提示缓存不足的解决方法

## 内核版本


## 问题现象
启动Tengine时提示缓存不足，报错“failed：no memory”。

## 问题根因
配置文件nginx.conf中未设置足够的共享内存缓存大小，导致Tengine启动时因缓存不足而失败。

## 解决方案
在nginx.conf配置文件的http块中添加缓存大小配置：执行命令 sed -i "/http {/a\check_shm_size 50m;" /usr/local/tengine-nginx/conf/nginx.conf，然后重新启动Tengine。

