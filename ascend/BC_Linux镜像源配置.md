# BC_Linux镜像源配置

## 内核版本


## 问题现象
在Atlas 300T训练卡（型号：9000）、Atlas 300T Pro训练卡（型号：9000）、Atlas 800训练服务器（型号：9000/9010）、Atlas 900计算节点、Atlas 900T RAK计算节点等产品环境中安装驱动时，出现安装失败，提示缺少dkms和kernel-headers包。

## 问题根因
系统未正确配置可用的软件源，导致无法通过yum安装驱动依赖的dkms和kernel-headers软件包。

## 解决方案
通过挂载系统安装ISO镜像并配置本地yum源解决：1. 备份原有repo文件；2. 在KVM界面挂载系统ISO镜像；3. 将ISO挂载到/mnt目录；4. 创建/etc/yum.repo.d/iso.repo文件，添加本地源配置；5. 执行yum clean all和yum makecache更新缓存；6. 验证repo列表确认配置成功。

