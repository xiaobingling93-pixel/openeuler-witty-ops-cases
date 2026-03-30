# 使用ascend-cert工具时提示CRL更新失败

## 内核版本


## 问题现象
使用ascend-cert工具的CRL更新功能时，报错提示“CRL update failed！”。

## 问题根因
保存的历史CRL超过上限，导致无法更新。

## 解决方案
删除历史CRL文件。root用户需手动删除/etc/hwsipcrl/ascendsip_g2.crl，非root用户需手动删除~/.local/hwsipcrl/ascendsip_g2.crl。

