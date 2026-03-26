# chaste安装过程中报错

## 内核版本


## 问题现象
运行 make -j48 Continuous 后报错，报错信息为：“AttributeError: 'str' object has no attribute 'format'”。

## 问题根因
代码中使用了 Python 2.6 新增的字符串格式化方法 .format()，但当前运行环境可能为不支持该方法的旧版本 Python（如 Python 2.5 或更早），导致 AttributeError。

## 解决方案
修改 translators.py 文件：将第1830行取消注释，第1831行注释掉；将第1838行取消注释，第1839行注释掉。具体路径为 /path/to/CHASTE/Chaste-release_2019.1/python/pycml/translators.py。修改后使用 std::cout 输出错误信息，避免调用 .format() 方法。

