# KVM如何使用图形化安装Guest OS

## 内核版本


## 问题现象
KVM图形化安装Guest OS时提示“X startup failed, falling back to text mode”。

## 问题根因
aarch64上的虚拟机目前只支持Virtio类型的显卡，要支持图形需要为虚拟机添加Virtio类型的视频设备、VNC类型的图形设备、Virtio Keyboard的输入设备和Virtio Tablet的输入设备、通用USB Keyboard。

## 解决方案
1. 在新建虚拟机时勾选“Customize configuration before install”。
2. 在弹出的配置窗口中单击“Add Hardware”。
3. 在弹出的窗口选择“Input”，下拉选择“Generic USB Keyboard”，单击“Finish”完成。
4. 继续选择“Input”，下拉选择“Virtio Keyboard”，单击“Finish”完成。
5. 继续选择“Input”，下拉选择“Virtio Tablet”，单击“Finish”完成。
6. 选择“Graphics”，“Type”下拉选择“VNC server”，单击“Finish”完成。
7. 选择“Video”，“Model”下拉选择“Virtio”，单击“Finish”完成。
8. 单击“Begin Installation”开始安装。

