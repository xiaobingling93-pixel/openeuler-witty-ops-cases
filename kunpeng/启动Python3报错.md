# 启动Python3报错

## 内核版本


## 问题现象
启动Python3时，提示无法找到libpython3.8.so.1.0。

## 问题根因
Python3运行时未加载到libpython3.8.so.1.0库文件。

## 解决方案
将解压后编译目录中的libpython3.8.so.1.0复制到库目录。
```
cp libpython3.8.so.1.0 /usr/local/lib64/
cp libpython3.8.so.1.0 /usr/lib64/
cp libpython3.8.so.1.0 /usr/lib/
```

