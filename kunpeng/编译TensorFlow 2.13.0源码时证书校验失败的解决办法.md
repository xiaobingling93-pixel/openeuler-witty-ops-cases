# 编译TensorFlow 2.13.0源码时证书校验失败的解决办法

## 内核版本


## 问题现象
执行编译TensorFlow 2.13.0命令时提示“unable to find valid certification path to requested target”证书校验失败，具体表现为Bazel在下载依赖（如rules_jvm_external、llvm等）时因SSL握手异常而失败，错误信息为：PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target。

## 问题根因
系统Java环境的信任证书库中缺少访问GitHub等外部资源所需的CA证书，导致SSL/TLS连接无法完成证书链验证。

## 解决方案
1. 使用浏览器（如Chrome）访问https://github.com，导出站点证书（如ca.crt）；2. 将该证书上传至服务器，并使用keytool命令将其导入Java的信任证书库，例如：keytool -import -alias tf_need -keystore /usr/lib/jvm/java-11-openjdk-11.0.21.9-1.oe2203sp3.aarch64/lib/security/cacerts -file ca.crt -trustcacerts -storepass changeit -noprompt；3. 验证证书是否导入成功：keytool -list -storepass changeit -keystore ... | grep tf_need；4. 重启服务器使配置生效；5. 重新执行bazel clean和bazel build命令进行编译。

