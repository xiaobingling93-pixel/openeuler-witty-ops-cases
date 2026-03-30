# 编译Nginx时提示未添加ngx_http_ssl_module的解决方法

## 内核版本


## 问题现象
已经编译安装好的Nginx，在添加未被编译的模块时，提示未添加ngx_http_ssl_module。错误信息为：nginx: [emerg] the "ssl" parameter requires ngx_http_ssl_module in /usr/local/nginx/conf/nginx.conf:100。

## 问题根因
Nginx在初始编译安装时未包含http_ssl_module模块，导致无法启用SSL相关功能。

## 解决方案
方法一：1. 使用/usr/local/nginx/sbin/nginx -V查看原有编译参数；2. 在源码目录执行./configure --with-http_ssl_module（可结合原有参数）；3. 执行make编译但不要make install；4. 备份原sbin/nginx文件；5. 停止Nginx服务；6. 将objs/nginx覆盖到sbin目录；7. 重启Nginx并验证模块是否加载成功。方法二：重新执行configure命令，显式添加--with-http_ssl_module及其他所需模块，并指定依赖路径（如--with-openssl=/home/openssl-1.1.1a），然后执行make -j80 && make install重新安装。

