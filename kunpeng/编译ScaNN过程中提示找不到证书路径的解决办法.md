# 编译ScaNN过程中提示找不到证书路径的解决办法

## 内核版本


## 问题现象
执行编译ScaNN命令时，Bazel在下载依赖（如bazel-skylib）过程中报错：'unable to find valid certification path to requested target'，导致构建失败。错误信息显示Java在通过HTTPS访问https://github.com时因SSL证书校验失败而无法下载资源。

## 问题根因
ScaNN编译过程中需要通过Java（Bazel底层使用）从https://github.com下载依赖，但系统Java环境的信任证书库（cacerts）中缺少访问该站点所需的根证书，导致SSL/TLS握手失败，无法建立安全连接。

## 解决方案
1. 使用浏览器访问https://github.com，导出站点证书（如ca.crt）；2. 将证书上传至服务器，并使用keytool命令将其导入Java的信任证书库（例如：keytool -import -alias ca -keystore /usr/lib/jvm/java-11-openjdk-.../lib/security/cacerts -file ca.crt -trustcacerts -storepass changeit -noprompt）；3. 验证证书是否导入成功（keytool -list ... | grep -w ca）；4. 重启设备；5. 重新配置网络代理、pip源、bazel及Python头文件环境变量；6. 重新执行编译命令。相关操作截图见原文中的图片链接：/doc_center/source/zh/SRA/ecosystemEnable/ScaNN/zh-cn_image_0000001955518472.png等。

