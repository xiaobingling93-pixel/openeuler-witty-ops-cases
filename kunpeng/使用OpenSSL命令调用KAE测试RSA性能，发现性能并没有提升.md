# 使用OpenSSL命令调用KAE测试RSA性能，发现性能并没有提升

## 内核版本
4.19或5.1x

## 问题现象
在鲲鹏920处理器的openEuler 20.03 LTS系统上，使用OpenSSL命令 './openssl speed -elapsed -engine kae rsa2048' 测试RSA性能时，未观察到性能提升。

## 问题根因
可能原因包括：1）硬件非鲲鹏处理器或License未正确加载；2）KAE安装方式与内核版本不匹配（RPM/DEB仅支持4.19内核，其他版本需源码编译）；3）OpenSSL环境变量未正确配置；4）KAE未成功安装或未被实际启用；5）实际运行时仍使用软件加密（libcrypto.so.1.1），而非KAE硬件加速。

## 解决方案
1. 确认使用鲲鹏处理器并通过 'lspci | grep HPRE' 和 'lspci | grep ZIP' 验证License已加载；2. 根据内核版本选择正确的KAE安装方式（4.19内核用kae1分支，5.1x内核用kae2分支，非4.19内核建议源码编译）；3. 确保OpenSSL版本为1.1.1a及以上并正确配置环境变量；4. 按照《鲲鹏加速引擎 用户指南》检查KAE是否安装成功；5. 运行测试时通过 'cat /sys/class/uacce/hisi_sec-1/attrs/available_instances' 查看队列消耗确认KAE启用，或通过 'perf top' 检查是否存在libcrypto.so.1.1以排除软加密。

