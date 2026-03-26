# 在 Atlas 500智能小站 WebUI上部署容器应用失败，提示“操作失败”

## 内核版本


## 问题现象
在Atlas 500智能小站 WebUI上部署容器应用时操作失败，界面提示“操作失败”。日志中可能出现“Invalid ImageFile”报错。

## 问题根因
镜像文件包内缺少cms数字签名和crl证书吊销列表，导致镜像文件校验失败。

## 解决方案
1. 使用SSH登录Atlas 500 CLI管理界面；2. 执行develop命令进入开发模式；3. 检查日志“/var/alog/AtlasEdge_log/edge_site/edge_site_run.log”是否存在“Invalid ImageFile”错误；4. 若存在该错误，请参考《MindX Edge 应用部署与模型更新指南》中关于通过WebUI部署容器应用的章节重新部署。

