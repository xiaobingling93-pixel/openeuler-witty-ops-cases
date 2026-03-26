# 运行迁移后代码报未定义API的错误

## 内核版本


## 问题现象
运行迁移后的代码时报未定义API的错误，该API出现在不支持API列表unsupported_api.csv中，且并非迁移前原始代码中使用的API。

## 问题根因
libcst 0.4.3之前的版本对形如“from a import b, bc”的导入语句存在解析问题。例如，当导入项中一个名称是另一个名称的前缀时（如from keras.datasets import cifar10, cifar100），迁移工具无法正确解析这些API，导致生成错误的迁移结果。

## 解决方案
将libcst库升级至0.4.3或更高版本，并重新执行脚本迁移。

