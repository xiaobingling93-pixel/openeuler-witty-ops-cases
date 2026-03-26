# spring-cloud-consul下载问题的解决方法

## 内核版本


## 问题现象
在编译环境中使用wget下载时出现“cannot verify certificate”错误，导致执行src/main/bash/travis_install_consul.sh脚本无法下载consul。

## 问题根因
wget在下载过程中进行SSL证书验证失败，而脚本默认未启用忽略证书验证的选项。

## 解决方案
修改src/main/bash/travis_install_consul.sh脚本中的IGNORE_CERTS变量默认值为"yes"，即把第5行代码从IGNORE_CERTS="${IGNORE_CERTS:-no}"改为IGNORE_CERTS="${IGNORE_CERTS:-yes}"，使wget命令带上--no-check-certificate选项跳过证书验证，然后重新执行该脚本。参考图示：/doc_center/source/zh/kunpengwebs/ecosystemEnable/SpringCloud/zh-cn_image_0000001171986266.png

