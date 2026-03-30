# 使用openssl.cnf调用KAE前后没有性能变化

## 内核版本


## 问题现象
已经参考《鲲鹏加速引擎 用户指南》中的“通过OpenSSL/Tongsuo配置文件openssl.cnf使用KAE”完成OPENSSL_CONF的配置，使用openssl speed -elapsed rsa2048和openssl speed -elapsed -engine kae rsa2048命令调用KAE前后发现性能没有变化。

## 问题根因
如果已经配置了OPENSSL_CONF环境变量，那么运行openssl speed -elapsed rsa2048和openssl speed -elapsed -engine kae rsa2048命令时KAE都会被调用，因此两次测试都使用了KAE，导致性能没有差异。

## 解决方案
1. 取消OPENSSL_CONF的配置：unset OPENSSL_CONF，并设置OPENSSL_ENGINES="/usr/local/lib/engines-1.1"；2. 进行未调用KAE的RSA性能测试：openssl speed -elapsed rsa2048；3. 重新设置OPENSSL_CONF环境变量：export OPENSSL_CONF=/home/app/openssl.cnf；4. 进行调用KAE的RSA性能测试：openssl speed -elapsed -engine kae rsa2048。预期结果是调用KAE后性能显著提升（例如鲲鹏920 7260处理器上从约750sign/s提升到约3000sign/s）。

