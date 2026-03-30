# 编译安装Hoverfly时提示cannot find package的解决方法

## 内核版本


## 问题现象
编译安装Hoverfly时提示“cannot find package”。

## 问题根因
系统缺少goproxy、logrus导致的问题。

## 解决方案
手动下载缺失的包：
```
go get -u github.com/SpectoLabs/goproxy
go get -u github.com/sirupsen/logrus
```

