# 鲲鹏DevKit卸载失败的解决方法

## 内核版本


## 问题现象
鲲鹏DevKit卸载失败，如图所示：![](/doc_center/source/zh/kunpengdevps/userguide/Plugins_UserGuide/figure/zh-cn_image_0000002158550181.png)

## 问题根因
服务器“/etc/ssh/sshd_config”配置文件中的MaxSessions值低于最少连接数（5），导致鲲鹏DevKit卸载失败。

## 解决方案
修改服务器“/etc/ssh/sshd_config”配置文件中的MaxSessions值，使其大于等于5。具体步骤：1. 执行命令 vim /etc/ssh/sshd_config 打开配置文件；2. 将MaxSessions值修改为不小于5，修改前后对比见图：修改前 ![](/doc_center/source/zh/kunpengdevps/userguide/Plugins_UserGuide/figure/zh-cn_image_0000002158668553.png)，修改后 ![](/doc_center/source/zh/kunpengdevps/userguide/Plugins_UserGuide/figure/zh-cn_image_0000002123468562.png)。

