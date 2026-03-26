# msSanitizer工具使用 "--cce-enable-sanitizer -g" 编译算子时出现 "InputSection too large" 错误

## 内核版本


## 问题现象
使用msSanitizer工具并启用"--cce-enable-sanitizer -g"编译选项编译算子时，链接阶段报错：ld.lld: error: InputSection too large for range extension thunk。

## 问题根因
算子链接时输入的代码段过大，超出了编译器默认支持的指令跳转范围。

## 解决方案
在原有编译选项"--cce-enable-sanitizer -g"后增加"-Xaicore-start -mcmodel=large -mllvm -cce-aicore-relax -Xaicore-end"，以启用编译器扩大跳转范围的特性。

