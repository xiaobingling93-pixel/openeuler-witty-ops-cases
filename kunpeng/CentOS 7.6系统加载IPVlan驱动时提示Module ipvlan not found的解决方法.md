# CentOS 7.6系统加载IPVlan驱动时提示Module ipvlan not found的解决方法

## 内核版本
CentOS 7.6默认内核（需升级至4.14）

## 问题现象
在CentOS 7.6系统中尝试加载IPVLAN驱动时，系统提示“Module ipvlan not found.”，无法正常使用IPVLAN功能。

## 问题根因
CentOS 7.6自带的默认内核版本不支持IPVLAN驱动，该功能需要内核版本至少为4.14并启用相关配置选项。

## 解决方案
1. 使用CentOS 7.6并升级或替换为4.14版本的内核；
2. 在内核编译配置中启用IPVLAN选项（CONFIG_IPVLAN）；
3. 重新编译并安装新内核；
4. 重启系统并选择新内核启动；
5. 手动加载IPVLAN驱动模块：insmod /usr/lib/modules/新内核名称/kernel/drivers/net/ipvlan/ipvlan.ko。

