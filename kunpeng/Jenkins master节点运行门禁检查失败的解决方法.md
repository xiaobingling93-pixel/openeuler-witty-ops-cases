# Jenkins master节点运行门禁检查失败的解决方法

## 内核版本


## 问题现象
运行门禁检查时报错，具体错误信息如图1所示（图片链接：/doc_center/source/zh/nativedevp/userguide/faq/figure/zh-cn_image_0000002187305857.jpg）。

## 问题根因
Jenkins用户没有门禁检查命令行工具的执行权限。

## 解决方案
1. 修改命令行工具的属主，并确保Jenkins用户对命令行工具所在文件夹路径有可执行权限，执行命令：chown -R jenkins:jenkins /DevKit_CLI_PATH/（参考图2，图片链接：/doc_center/source/zh/nativedevp/userguide/faq/figure/zh-cn_image_0000002151868674.png）；2. 在Jenkins环境中重新添加用于实现具体业务的工作节点，避免使用内置节点“Built-In Node”。

