# 执行ascend-dmi --dg，诊断结果提示：hccn_tool no certificate found

## 内核版本


## 问题现象
执行ascend-dmi --dg命令时，诊断结果提示：hccn_tool no certificate found。

## 问题根因
找不到LTS证书或LTS证书已过期。

## 解决方案
使用HCCN Tool工具配置证书，示例如下：hccn_tool -i 0 -tls -s path /root pri pri.pem pub pub.pem ca1 ca1.pem ca2 ca2.pem crl xxx.crl。详细说明请参见预置或替换证书套件文档。

