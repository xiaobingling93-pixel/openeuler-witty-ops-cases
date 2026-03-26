# spring-cloud-contract异常，GitStubDownloaderTest用例提示异常的解决方法

## 内核版本


## 问题现象
编译安装过程中，执行GitStubDownloaderTest用例时，提示“Caused by: java.nio.file.NoSuchFileException: /tmp/git-contracts-1590371014299-0/.git/gc.log.lock”。

## 问题根因
GC（Garbage Collection）运行异常导致的问题。

## 解决方案
1. 打开GitStubDownloaderTests.java文件：vim spring-cloud-contract-stub-runner/src/test/java/org/springframework/cloud/contract/stubrunner/GitStubDownloaderTests.java
2. 搜索map找到props()方法，添加如下内容：
map.put("gc.auto", "0");
map.put("gc.autoPackLimit", "0");
map.put("receive.autogc", "false");
3. 保存并退出编辑。
4. 重新执行编译命令：./mvnw clean install -Dgpg.skip=true

