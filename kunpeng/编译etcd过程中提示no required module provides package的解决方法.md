# 编译etcd过程中提示no required module provides package的解决方法

## 内核版本


## 问题现象
编译etcd过程中提示“no required module provides package github.com/coreos/etcd/cmd/etcd: go.mod file not found”。

## 问题根因
GO111MODULE模块未打开。

## 解决方案
1. 打开GO111MODULE模块：执行命令 `go env -w GO111MODULE=auto`。
2. 重新编译etcd：执行命令 `./build`。

