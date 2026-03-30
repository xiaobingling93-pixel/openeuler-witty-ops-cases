# 尝试打印Device侧的Tensor、Image内存数据时，发生coredump

## 内核版本


## 问题现象
当Tensor、Image类数据在Device侧时，尝试调用GetData()接口返回指针并打印指针所指向的数据时，出现coredump。

## 问题根因
Device侧地址空间与Host侧地址空间相互独立，Host侧无法直接访问Device侧数据。

## 解决方案
请先使用Tensor.ToHost()接口或Image.ToHost()接口，将Device侧Tensor类或Image类数据转移到Host侧后，再次尝试打印数据操作。

