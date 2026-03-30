# 使用KML_LAPACK库求矩阵的逆时提示缺少库文件的解决办法

## 内核版本


## 问题现象
在使用KML中的LAPACK库调用dpotri_函数求矩阵逆时，动态编译失败，链接器报错显示libklapack.so中存在多个未定义引用（如zgebrd_、sgerqf_netlib_等）。环境变量已正确设置，但ldd显示libklapack.so未链接到必要的Netlib LAPACK相关库。

## 问题根因
鲲鹏数学库（KML）RPM包中提供的LAPACK库不完整，缺少部分函数实现，必须与开源的Netlib LAPACK结合使用才能构成完整的LAPACK库。当前编译未包含Netlib LAPACK，导致链接时缺失符号定义。

## 解决方案
按照《鲲鹏数学库 开发指南》中“生成完整的LAPACK”章节的说明，结合开源Netlib LAPACK构建完整的LAPACK库，并在编译链接时正确引入该完整库。

