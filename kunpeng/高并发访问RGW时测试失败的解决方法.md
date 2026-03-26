# 高并发访问RGW时测试失败的解决方法

## 内核版本


## 问题现象
当RGW（RADOS Gateway）的访问并发数大于512时，COSBench测试异常终止，日志中出现'HTTP Request Time Out'错误，同时RGW日志显示'iterate_obj() failed with -5'。

## 问题根因
RGW默认线程数（rgw_thread_pool_size）为512，当并发请求数超过该值时，RGW无法处理额外的请求，导致所有测试失败。

## 解决方案
通过修改ceph.conf配置文件，将RGW前端线程数增加至1024：执行命令 sed -i 's/rgw_frontends.*/& num_threads=1024/g' ceph.conf，然后重启RGW服务：systemctl restart ceph-radosgw.target。

