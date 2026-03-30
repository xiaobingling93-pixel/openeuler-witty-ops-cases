# kml_fft库函数执行代码提示Illegal instruction core dumped的解决办法

## 内核版本


## 问题现象
Euler 2.0系统下通过rpm2cpio xxx.rpm | cpio -div解压到本地安装BoostKit-kml 2.0.0后，运行调用kml_fft函数时提示“Illegal instruction core dumped”。

## 问题根因
未通过rpm命令直接安装鲲鹏数学库，且未使用正确的so库。kfft-neon目录下的so库支持NEON指令，lib目录下的so库支持SVE指令，而运行环境可能不支持SVE指令。

## 解决方案
检查环境是否支持SVE指令，若不支持，则使用kfft-neon中的so库进行编译。建议后续使用rpm方式安装数学库以确保正确性。

