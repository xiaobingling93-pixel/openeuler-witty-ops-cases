# 链接KML_VML动态库失败的解决办法

## 内核版本


## 问题现象
使用KML_VML单线程版本编译时，添加动态库路径 -L /usr/local/kml/lib/kvml/single -lkvml -lkm 后，链接报错：/usr/bin/ld: /usr/local/kml/lib/kvml/single/libkvml.so: undefined reference to `sindf'、`tanpif'、`powrf'、`acospi' 等符号。

## 问题根因
编译链接选项中缺少必要的数学库（libm）以及其他依赖库，导致链接器无法解析 libkvml.so 中引用的数学函数符号。

## 解决方案
在编译命令中补充缺失的库路径和库文件，修改为：g++ -L /usr/local/kml/lib/kvml/single -lkvml -L /usr/local/kml/lib -lkm -lm，其中 -lm 链接标准数学库以提供缺失的数学函数符号。

