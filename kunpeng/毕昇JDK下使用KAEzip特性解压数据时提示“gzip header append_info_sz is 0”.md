# 毕昇JDK下使用KAEzip特性解压数据时提示“gzip header append_info_sz is 0”

## 内核版本


## 问题现象
在毕昇JDK下使用KAEzip特性解压零字节数组压缩后的文件时，执行java -DGZIP_USE_KAE=true 测试文件命令进行解压缩后提示“gzip header append_info_sz is 0”。前提条件是环境中已部署8u422及以上版本的毕昇JDK和2.0.3以下版本的KAE。

## 问题根因
KAEzip压缩后的文件格式与Gzip文件格式不一致，导致文件无法被正确解压。

## 解决方案
该问题已在KAE最新版本中解决，请获取最新版本的KAE安装后重新执行用例。KAE最新版本获取链接：https://www.hikunpeng.com/zh/developer/boostkit/compress

