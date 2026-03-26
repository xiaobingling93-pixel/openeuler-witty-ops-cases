# 安装OPTIMIZED-ROUTINES执行make编译时报错

## 内核版本


## 问题现象
安装OPTIMIZED-ROUTINES执行make编译时，提示“/usr/bin/ld: cannot find -lm”和“/usr/bin/ld: cannot find –lc”。

## 问题根因
缺少环境依赖。

## 解决方案
请执行以下命令：

```
yum install -y glibc-static
```

