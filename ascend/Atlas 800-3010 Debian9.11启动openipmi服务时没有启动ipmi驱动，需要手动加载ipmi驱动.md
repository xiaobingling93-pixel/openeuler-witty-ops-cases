# Atlas 800-3010 Debian9.11启动openipmi服务时没有启动ipmi驱动，需要手动加载ipmi驱动

## 内核版本


## 问题现象
在Debian 9.11系统上安装并启动openipmi服务后，执行ipmitool命令失败，提示无法与BMC通信或设备不存在，原因是系统未自动加载IPMI内核驱动。

## 问题根因
Debian 9.11系统在启动openipmi服务时不会自动加载ipmi_si等必要的IPMI内核模块，而ipmitool依赖这些内核驱动提供系统接口，因此必须手动加载驱动才能正常使用。

## 解决方案
执行命令 'modprobe ipmi_si' 手动加载IPMI驱动模块，之后即可正常使用ipmitool。与RHEL系统不同，Debian 9.11无法通过配置文件（如/etc/sysconfig/ipmi）自动启用驱动，必须显式加载。

