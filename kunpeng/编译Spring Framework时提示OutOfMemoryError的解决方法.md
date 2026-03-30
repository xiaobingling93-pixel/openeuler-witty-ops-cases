# 编译Spring Framework时提示OutOfMemoryError的解决方法

## 内核版本


## 问题现象
编译Spring Framework过程中提示“OutOfMemoryError thrown from UncaughtExceptionHandler”。

## 问题根因
内存溢出（Out Of Memory）导致，需要调大内存设置。

## 解决方案
1. 打开build.gradle文件（vim build.gradle）。
2. 在第338行和第339行添加配置：minHeapSize = "4096m" 和 maxHeapSize = "4096m"。
3. 保存并退出编辑（按“Esc”键，输入:wq!，按“Enter”）。
4. 重新编译Spring Framework。
参考图片：/doc_center/source/zh/kunpengwebs/ecosystemEnable/SpringFramework/zh-cn_image_0000001171821984.png

