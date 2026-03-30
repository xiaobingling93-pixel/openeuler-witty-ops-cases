# 通过VNC访问KVM虚拟机，VNC无响应的解决方法

## 内核版本


## 问题现象
在鲲鹏服务器上安装CentOS 7.6后，使用KVM虚拟化方案，通过VNC接入创建好的虚拟机后，无法通过VNC进行操作。具体现象为：通过VNC登录虚拟机后，无法输入任何字符，且界面无响应。

## 问题根因
ARM服务器中，虚拟机不支持使用PS2总线连接的鼠标作为输入设备，而虚拟机配置文件中仅定义了使用PS2总线的鼠标，未配置键盘，导致VNC无响应。

## 解决方案
1. 关闭虚拟机：virsh shutdown centos；
2. 修改虚拟机配置：virsh edit centos，将<input type='mouse' bus='ps2'/>改为<input type='mouse' bus='virtio'/>
并添加<input type='keyboard' bus='virtio'/>；
3. 保存配置并重启虚拟机：virsh start centos；
4. 验证配置已生效：virsh dumpxml centos；
5. 再次通过VNC登录虚拟机，即可正常操作。

