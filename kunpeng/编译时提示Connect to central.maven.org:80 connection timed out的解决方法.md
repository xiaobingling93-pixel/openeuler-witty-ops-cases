# 编译时提示Connect to central.maven.org:80 connection timed out的解决方法

## 内核版本


## 问题现象
编译时出现错误，提示 'Failed Connect to central.maven.org:80 connection timed out'。

## 问题根因


## 解决方案
1. 打开“java/Makefile”文件；2. 修改文件第190行的Maven仓库地址为https://repo1.maven.org/maven2/，即设置 CENTRAL_REPO_URL?=https://repo1.maven.org/maven2/；3. 保存并退出编辑。

