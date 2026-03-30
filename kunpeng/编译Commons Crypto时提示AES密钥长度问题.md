# 编译Commons Crypto时提示AES密钥长度问题

## 内核版本


## 问题现象
执行编译Commons Crypto时提示测试要求支持AES密钥长度为256，但检测到的最大密钥长度为128，导致测试失败（JceCipherTest.checkJceUnlimitedStrength:44）。

## 问题根因
测试环境缺少Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files，导致Java运行时仅支持最大128位的AES密钥长度。

## 解决方案
1. 下载jce_policy-8.zip并解压；2. 将解压得到的local_policy.jar和US_export_policy.jar复制到$JAVA_HOME/jre/lib/security目录下；3. 通过Yum安装依赖库：yum install libstdc++-static.aarch64 -y 和 yum install glibc* -y。

