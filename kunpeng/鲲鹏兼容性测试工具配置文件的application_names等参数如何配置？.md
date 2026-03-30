# 鲲鹏兼容性测试工具配置文件的application_names等参数如何配置？

## 内核版本


## 问题现象
用户不清楚如何正确配置鲲鹏兼容性测试工具配置文件中的application_names、start_app_commands、stop_app_commands等参数；此外还涉及apt/yum源不可用、测试环境非空（存在高资源占用进程）、以及网卡驱动导致ksoftirqd进程占满CPU等问题。

## 问题根因
缺乏对配置参数语义和使用场景的理解；系统软件源配置不正确或不可达；测试前未清理系统环境，存在干扰进程；服务器网卡驱动版本过旧，引发软中断处理进程ksoftirqd异常占用CPU资源。

## 解决方案
1. application_names应填写可通过ps -ef | grep匹配到的应用进程名（如tomcat-juli.jar、mysqld），多个以逗号分隔；2. start_app_commands支持目录切换、用户切换及顺序启动脚本；3. 若无压力测试工具，可留空start_performance_scripts并在提示时手动执行；4. 针对apt/yum源不可用，需配置可用本地或远程源并安装对应依赖包（如nmap、ipmitool、sysstat等）；5. 测试前检查系统资源占用，使用top、iostat、netstat等命令定位并停止高负载进程；6. 若ksoftirqd占用CPU 100%，需升级网卡驱动（如安装hinic驱动RPM包：rpm -ivh NIC-IN200-CentOS7.6-hinic-xxxx-aarch64.rpm，再通过rmmod/modprobe加载，并验证版本）。相关操作示例和截图见文档内嵌图片链接。

