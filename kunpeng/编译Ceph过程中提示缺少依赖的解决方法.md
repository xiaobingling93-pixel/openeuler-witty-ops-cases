# 编译Ceph过程中提示缺少依赖的解决方法

## 内核版本


## 问题现象
为使能EC Turbo特性，编译Ceph时提示“Could NOT find LTTngUST (missing: LTTNGUST_LIBRARIES LTTNGUST_INCLUDE_DIRS)”。

## 问题根因
环境上缺少对应的开源三方依赖包。

## 解决方案
根据报错信息安装所需依赖包：yum install -y lttng-ust-devel keyutils-libs-devel openldap-devel leveldb-devel snappy-devel lz4-devel curl-devel expat-devel openssl-devel libbabeltrace-devel librabbitmq-devel rdma-core-devel python2-Cython python3-Cython

