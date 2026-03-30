# root用户切换到普通用户需要输入密码权限

## 内核版本


## 问题现象
在Atlas 300I Pro推理卡、Atlas 300V Pro视频解析卡、Atlas 300I Duo推理卡、Atlas 300V视频解析卡产品环境的软件包安装过程中，出现“The Root use cmd(su user) must enter the user passwd forcibly(set by /etc/pam.d/su)”报错，表明root用户使用su命令切换到普通用户时被强制要求输入该普通用户的密码。

## 问题根因
系统配置文件“/etc/pam.d/su”中默认注释掉了“auth sufficient pam_rootok.so”这一行，导致root用户执行su命令切换到其他用户时仍需输入目标用户的密码。

## 解决方案
有两种解决方法：1. 直接输入目标运行用户的密码以继续完成安装；2. 修改“/etc/pam.d/su”配置文件，取消注释“auth sufficient pam_rootok.so”行，使root用户切换到其他用户时无需输入密码。具体操作为：执行“vi /etc/pam.d/su”，删除“auth sufficient pam_rootok.so”前的“#”号，保存并退出。

