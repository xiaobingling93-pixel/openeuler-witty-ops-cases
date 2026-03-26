# 编译etcd过程中提示Needed a single revision的解决方法

## 内核版本


## 问题现象
编译etcd过程中提示“fatal: Needed a single revision”。

## 问题根因
etcd在编译过程中会将本地代码与远程代码进行比较（校对），执行build时脚本会因无法获取单一修订版本而停止。

## 解决方案
1. 进入“etcd-3.1.20”目录；2. 打开build文件；3. 将第9-12行代码注释掉（参考图片：/doc_center/source/zh/kunpengdbs/ecosystemEnable/Etcd/zh-cn_image_0000001640789453.png）；4. 保存并退出编辑；5. 重新执行./build命令进行编译。

