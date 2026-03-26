# 编译FreeIPA失败的解决方法

## 内核版本


## 问题现象
编译FreeIPA软件包时提示“Installed (but unpackaged) file(s) found: /usr/share/selinux/packages/targeted/ipa.pp.bz2”。

## 问题根因
rpm-build软件包与FreeIPA软件包的SPEC文件存在兼容性问题。

## 解决方案
1. 修改“freeipa/freeipa.spec”文件，将相关行注释掉（参考图片：/doc_center/source/zh/kunpengcpfs/ecosystemEnable/oVirt/zh-cn_image_0000002159164946.png 和 /doc_center/source/zh/kunpengcpfs/ecosystemEnable/oVirt/zh-cn_image_0000002194525813.png）。
2. 重新编译FreeIPA软件包。

