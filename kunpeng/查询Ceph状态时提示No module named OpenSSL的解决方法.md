# 查询Ceph状态时提示No module named OpenSSL的解决方法

## 内核版本


## 问题现象
查询Ceph状态时报告“No module named OpenSSL”。

## 问题根因
系统缺少Python的OpenSSL模块（pyOpenSSL）。

## 解决方案
安装对应Python版本的pyOpenSSL包：
```bash
yum install python2-pyOpenSSL.noarch
yum install python3-pyOpenSSL.noarch
```

