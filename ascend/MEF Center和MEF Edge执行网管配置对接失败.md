# MEF Center和MEF Edge执行网管配置对接失败

## 内核版本


## 问题现象
MEF Center和MEF Edge执行网管配置命令失败，回显提示“Execute [netconfig] command failed!”。

## 问题根因
可能的原因包括：1）提供的token不正确，导致认证失败（HTTP 401错误）；2）连续认证失败超过5次后IP被锁定5分钟（HTTP 423错误）；3）MEF Center与MEF Edge之间网络不通或网管配置参数错误。

## 解决方案
1. 查看MEF Edge安装日志（/var/alog/MEFEdge_log/edge_installer/edge_installer_run.log）定位具体错误；2. 若为token错误，确认token正确性并在锁定时间（5分钟）过后重试；3. 若为其他错误，检查网络连通性及配置参数是否正确；4. 参考《MEF用户指南》重新进行认证对接。

