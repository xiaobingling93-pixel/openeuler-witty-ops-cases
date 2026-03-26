# 编译libnice时gst插件的libgstnice动态库无法生成问题的解决方法

## 内核版本


## 问题现象
在Ubuntu 18.04系统上，使用已编译完成的GStreamer 1.5版本编译libnice时，未能生成gst插件所需的libgstnice.so动态库。

## 问题根因
libnice的configure脚本默认仅检测gstreamer-1.0相关组件，当系统中安装的是gstreamer-1.5时，configure无法识别，因此跳过了gst插件的编译流程。

## 解决方案
手动修改libnice源码中的configure文件，将其中所有与gstreamer-1.0相关的字符串替换为gstreamer-1.5，具体命令如下：
sed -i s/gstreamer-1.0/gstreamer-1.5/g configure
sed -i s/gstreamer-base-1.0/gstreamer-base-1.5/g configure
sed -i s/gstreamer-check-1.0/gstreamer-check-1.5/g configure
sed -i s/GST_MAJORMINOR=1.0/GST_MAJORMINOR=1.5/g configure
修改完成后重新运行configure并编译，即可成功生成libgstnice.so。

