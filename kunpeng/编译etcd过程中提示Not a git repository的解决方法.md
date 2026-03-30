# 编译etcd过程中提示Not a git repository的解决方法

## 内核版本


## 问题现象
编译etcd过程中提示“Not a git repository”。

## 问题根因
Git未初始化。

## 解决方案
1. 初始化Git：执行命令 `git init`。
2. 重新编译etcd：执行命令 `./build`。

