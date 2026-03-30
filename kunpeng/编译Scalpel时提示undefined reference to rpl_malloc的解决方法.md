# 编译Scalpel时提示undefined reference to rpl_malloc的解决方法

## 内核版本


## 问题现象
使用make命令编译Scalpel过程中提示“undefined reference to rpl_malloc”。

## 问题根因
confdefs.h文件中存在宏定义“#define malloc rpl_malloc”和“#define realloc rpl_realloc”，这是由于autotools在交叉编译时误判工具链的libc中不包含malloc和realloc函数，从而引入了这些替换宏，但实际链接时找不到rpl_malloc和rpl_realloc的实现，导致链接错误。

## 解决方案
1. 打开configure文件。
2. 删除以下两行：
   - $as_echo "define malloc rpl_malloc" >>confdefs.h
   - $as_echo "define realloc rpl_realloc" >>confdefs.h
3. 保存并退出，重新执行编译命令。

