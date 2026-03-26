# 编译时显示构建boringssl失败的解决方法

## 内核版本


## 问题现象
编译时显示构建BoringSSL失败，提示“Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run(build-boringssl)”。

## 问题根因
使用go get等命令时，golang.org/x/...等包因网络限制无法直接下载，导致BoringSSL依赖获取失败。Go 1.11起引入GOPROXY机制，若未配置代理，则无法正常拉取所需模块。

## 解决方案
1. 确认Go版本；2. 编辑/etc/profile文件，添加环境变量：export GOPROXY=https://goproxy.io 和 export GO111MODULE=on；3. 使环境变量生效（source /etc/profile）；4. 删除旧的boringssl-chromium-stable目录；5. 拷贝新的boringssl-chromium-stable到指定路径；6. 重新执行mvn clean install进行编译。

