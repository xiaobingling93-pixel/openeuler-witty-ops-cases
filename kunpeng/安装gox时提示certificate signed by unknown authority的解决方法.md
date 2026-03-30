# 安装gox时提示certificate signed by unknown authority的解决方法

## 内核版本


## 问题现象
安装gox时提示“x509: certificate signed by unknown authority”。

## 问题根因
系统不能识别到根证书导致的问题。

## 解决方案
1. 创建证书文件：vim /etc/pki/ca-trust/source/anchors/huawei.crt
2. 按“i”进入编辑模式，添加指定的华为根证书内容。
3. 按“Esc”键，输入:wq!保存并退出。
4. 更新CA文件：update-ca-trust extract
5. 查看证书文件确认内容：cat /etc/pki/ca-trust/source/anchors/huawei.crt
6. 重新执行命令获取并安装gox：go get github.com/mitchellh/gox

