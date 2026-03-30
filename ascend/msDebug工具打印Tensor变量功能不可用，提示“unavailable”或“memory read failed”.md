# msDebug工具打印Tensor变量功能不可用，提示“unavailable”或“memory read failed”

## 内核版本


## 问题现象
使用msDebug工具打印Tensor变量时，提示“unavailable”或“Failed to dereference pointer from xxx for DW_OP_deref: memory read failed for xxx”。

## 问题根因
单步调试功能不支持Tensor按值传递的写法，当Tensor类型变量以值传递方式作为函数入参时，调试器无法正确读取其内存内容。

## 解决方案
将Tensor类型的函数参数由值传递修改为引用传递。例如，将 void Foo(const LocalTensor<float> a); 修改为 void Foo(const LocalTensor<float> &a); 即可正常打印该变量。

