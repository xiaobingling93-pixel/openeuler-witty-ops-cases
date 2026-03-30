# 编译MySQL时提示unsupported platform的解决方法

## 内核版本


## 问题现象
编译MySQL时，提示“unsupported platform”。

## 问题根因
由于没有定义ARM平台的宏定义导致。

## 解决方案
1. 修改os0atomic.h文件：打开/home/mysql-8/mysql-8.0.16/storage/innobase/include/os0atomic.h，找到#define IB_STRONG_MEMORY_MODEL，在其下方添加#else和#define HAVE_ATOMIC_BUILTINS两行。2. 修改os0atomic.ic文件：打开/home/mysql-8/mysql-8.0.16/storage/innobase/include/os0atomic.ic，将#elif defined(IB_STRONG_MEMORY_MODEL)改为#elif defined(HAVE_ATOMIC_BUILTINS)。3. 重新编译MySQL。

