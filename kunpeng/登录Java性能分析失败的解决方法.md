# 登录Java性能分析失败的解决方法

## 内核版本


## 问题现象
工具安装完成后可以成功登录鲲鹏DevKit，但使用Java性能分析功能失败；执行 netstat -anp | grep 19090 命令查询发现19090端口未被占用。

## 问题根因
Linux操作系统下 $JAVA_HOME/conf/security/java.security 文件中默认配置 securerandom.source=file:/dev/random，而 /dev/random 的 random pool 依赖系统中断，在中断数不足时会阻塞读取进程，导致Java性能分析服务启动延迟。

## 解决方案
1. 执行 vi $JAVA_HOME/conf/security/java.security 命令编辑 java.security 文件；
2. 将 securerandom.source=file:/dev/random 修改为 securerandom.source=file:/dev/urandom；
3. 保存并退出后，执行 systemctl restart java_perf 命令重启工具。

