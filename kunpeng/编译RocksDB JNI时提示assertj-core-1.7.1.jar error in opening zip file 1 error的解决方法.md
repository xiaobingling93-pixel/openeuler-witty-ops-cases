# 编译RocksDB JNI时提示assertj-core-1.7.1.jar error in opening zip file 1 error的解决方法

## 内核版本


## 问题现象
编译RocksDB JNI时提示不能打开assertj-core-1.7.1.jar，错误信息为：error reading test-libs/assertj-core-1.7.1.jar; error in opening zip file。

## 问题根因


## 解决方案
手动从Maven仓库下载assertj-core-1.7.1.jar及assertj-core-1.7.1.pom文件，并将它们放到本地仓库目录“/org/assertj/assertj-core/1.7.1”下。

