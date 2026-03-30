# 执行DevKit命令行工具命令时，提示“command not found”

## 内核版本


## 问题现象
执行DevKit命令时，系统提示“command not found”，如图所示：![](/doc_center/source/zh/kunpengdevps/userguide/cliuserguide/figure/zh-cn_image_0000002063903252.png)

## 问题根因
可能用户未正确安装DevKit命令行工具。

## 解决方案
1. 验证DevKit命令行工具是否正确安装：
   - 若以RPM包方式安装，执行命令 `rpm -qa | grep devkit`，若有回显信息（如图：![](/doc_center/source/zh/kunpengdevps/userguide/cliuserguide/figure/zh-cn_image_0000002100061697.png)），表示已安装。
   - 若以压缩包解压方式安装，可执行查看帮助命令，若有回显信息（如图：![](/doc_center/source/zh/kunpengdevps/userguide/cliuserguide/figure/zh-cn_image_0000002064061548.png)），表示已安装。
2. 若无对应回显信息，表示工具未安装，请参考官方文档重新安装DevKit命令行工具。

