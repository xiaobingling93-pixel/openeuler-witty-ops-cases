# Linux桌面系统使用Java性能分析工具，添加目标环境提示安装根目录但导入证书选项不可用

## 内核版本


## 问题现象
在Linux桌面系统中使用Java性能分析工具时，添加目标环境提示需要安装根目录，但界面上的导入证书选项不可用。

## 问题根因
该场景不在鲲鹏DevKit的规划支持范围内，内部未进行过相关环境验证，因此工具未提供图形界面的证书导入功能。

## 解决方案
建议手动导入证书：1. 下载ca.crt证书文件；2. 将其拷贝至系统证书目录（如CentOS/RHEL系为/etc/pki/ca-trust/source/anchors/，Ubuntu系为/usr/local/share/ca-certificates/或/usr/share/ca-certificates/）；3. 执行update-ca-trust extract（CentOS/RHEL）或update-ca-certificates（Ubuntu）命令加载证书；4. 重启CodeArts IDE后重新尝试添加节点。

