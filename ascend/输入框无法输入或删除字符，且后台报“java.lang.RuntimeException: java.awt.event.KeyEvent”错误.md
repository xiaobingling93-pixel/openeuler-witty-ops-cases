# 输入框无法输入或删除字符，且后台报“java.lang.RuntimeException: java.awt.event.KeyEvent”错误

## 内核版本


## 问题现象
在使用Windows通过另一台Windows远程连接一台Linux设备上的MindStudio时，出现输入框无法输入或删除字符，且后台报“java.lang.RuntimeException: java.awt.event.KeyEvent”错误。

## 问题根因
由于Windows远程连接和X11转发这两个过程存在键盘间的相互映射，如果这种映射关系不正确，就会导致键盘键入不能够被正确识别。

## 解决方案
1. 在Linux上通过localectl命令查看设备的键盘配置，获取X11 Layout值；2. 在MobaXterm中进入Settings > Configuration > X11页签，取消勾选“Unix-compatible Keyboard”，并将Keyboard设置为步骤1中查询到的X11 Layout值；3. 若问题仍未解决，重启MindStudio。

