# 安装glide时提示unrecognized import path的解决方法

## 内核版本


## 问题现象
安装glide时提示“unrecognized import path \"golang.org/x/sys/unix\"”。

## 问题根因
系统环境网络无法访问golang.org导致的问题。

## 解决方案
1. 查看go的版本（go version）。
2. 打开profile文件（vim /etc/profile）。
3. 添加环境变量：export GOPROXY=https://goproxy.io 和 export GO111MODULE=on。
4. 保存并退出编辑，使环境变量生效（source /etc/profile）。
5. 验证环境变量（echo $GOPROXY 和 echo $GO111MODULE）。
6. 重新安装glide（go get github.com/Sirupsen/logrus;）。

