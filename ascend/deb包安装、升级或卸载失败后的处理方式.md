# deb包安装、升级或卸载失败后的处理方式

## 内核版本


## 问题现象
Atlas系列硬件（包括Atlas 300I Pro推理卡、Atlas 300V Pro视频解析卡、Atlas 300I Duo推理卡、Atlas 300V视频解析卡、Atlas 300T训练卡、Atlas 300T Pro训练卡、Atlas 800训练服务器、Atlas 900计算节点等）在deb包安装、升级或卸载失败后，系统中残留的缓存信息会导致再次安装或升级时出现异常。

## 问题根因
deb包安装、升级或卸载失败后，dpkg未完全清理相关配置文件和安装目录中的残留文件，导致后续操作因状态不一致或文件冲突而失败。

## 解决方案
手动清理残留信息，具体步骤如下：1. 删除失败包的配置文件列表，例如执行命令 'rm /var/lib/dpkg/info/ascend910-driver*'；2. 执行强制删除命令 'dpkg --remove --force-remove-reinstreq ascend910-driver'；3. 删除原安装目录下的残留文件，例如 'rm -rf /usr/local/Ascend/driver'（以实际安装路径为准）。

