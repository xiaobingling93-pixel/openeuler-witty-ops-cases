# 编译TensorFlow 1.15.5时提示证书校验失败的解决办法

## 内核版本


## 问题现象
执行编译TensorFlow 1.15.5命令时提示“unable to find valid certification path to requested target”证书校验失败，具体错误为：PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target。

## 问题根因
下载依赖组件时，Java运行环境的信任证书库中缺少访问目标站点（如GitHub）所需的CA证书，导致SSL/TLS握手过程中无法验证服务器证书的有效性。

## 解决方案
1. 使用浏览器（如谷歌浏览器）访问目标网站（如GitHub），导出其CA证书（如ca.crt）。
2. 将导出的证书上传至服务器，并使用keytool命令将其导入Java的信任证书库（cacerts），例如：keytool -import -alias ca -keystore /usr/lib/jvm/java-11-openjdk-11.0.21.9-1.oe2203sp3.aarch64/lib/security/cacerts -file ca.crt -trustcacerts -storepass changeit -noprompt。
3. 验证证书是否导入成功：keytool -list -storepass changeit -keystore /usr/lib/jvm/java-11-openjdk-.../cacerts | grep -w ca。
4. 重启设备（reboot）。
5. 重新配置TensorFlow编译环境，包括设置网络代理、pip源、Bazel和Python环境变量。
6. 重新执行编译命令：bazel build --config=v1 --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" //tensorflow/tools/pip_package:build_pip_package。

