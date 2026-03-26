# 编译CMAKE时报The std::unique_ptr错误

## 内核版本


## 问题现象
编译CMAKE时出现错误："CMake Error at CMakeLists.txt:92 (message): The C++ compiler does not support C++11 (e.g. std::unique_ptr)."

## 问题根因
此错误与系统时间设置不正确有关。

## 解决方案
方法一：正确设定系统时间后，重新解压源码包进行编译。方法二：手动修改CmakeCache.txt文件，将第362行改为"CMake_HAVE_CXX_UNIQUE_PTR:INTERNAL=ON"，保存后重新执行make编译。

