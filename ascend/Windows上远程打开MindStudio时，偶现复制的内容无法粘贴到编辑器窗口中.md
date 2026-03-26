# Windows上远程打开MindStudio时，偶现复制的内容无法粘贴到编辑器窗口中

## 内核版本


## 问题现象
在Windows系统上通过远程方式打开MindStudio时，偶尔会出现从外部复制的内容无法粘贴到MindStudio编辑器窗口中的问题。

## 问题根因
MobaXterm自带的“划取即复制”（select on copy）功能与MindStudio的剪贴板机制冲突，导致复制内容无法正常粘贴。

## 解决方案
1. 在MobaXterm中禁用“select on copy”功能：进入设置，将“Clipboard”选项中的“select on copy”设为disable。2. 在MindStudio中关闭自动复制选中内容的功能：打开Settings > Tools > Terminal，取消勾选“Copy to clipboard on selection”。此外，也可在复制内容后避免在编辑器中再次选中内容，直接粘贴即可。

