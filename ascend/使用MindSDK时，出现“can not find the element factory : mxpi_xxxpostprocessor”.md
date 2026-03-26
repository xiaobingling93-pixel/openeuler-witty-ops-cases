# 使用MindSDK时，出现“can not find the element factory : mxpi_xxxpostprocessor”

## 内核版本


## 问题现象
使用MindSDK进行应用开发时，出现“can not find the element factory : mxpi_xxxpostprocessor”提示。即使在$HOME/SDK/mxManufacture-{version}/opensource/bin路径下执行./gst-inspect-1.0 mxpi_xxxpostprocessor确认插件能正常加载，运行时仍报相同错误。

## 问题根因
gstreamer的历史缓存没有清除。

## 解决方案
1. 确认环境已安装python3.9。
2. 执行 rm ~/.cache/gstreamer-1.0/registry.*x86_64*.bin（根据具体运行环境选择x86_64.bin或者aarch64.bin）来清除gstreamer的历史缓存，再运行程序即可。

