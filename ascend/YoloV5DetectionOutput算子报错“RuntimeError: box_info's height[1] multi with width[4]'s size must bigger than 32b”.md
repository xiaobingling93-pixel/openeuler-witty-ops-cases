# YoloV5DetectionOutput算子报错“RuntimeError: box_info's height[1] multi with width[4]'s size must bigger than 32b”

## 内核版本


## 问题现象
在自定义网络中，对数据先进行nms后处理，再使用YoloV5DetectionOutput算子，通过atc工具转换模型时出现报错：RuntimeError: box_info's height[1] multi with width[4]'s size must bigger than 32b。

## 问题根因
使用YoloV5DetectionOutput算子处理经过nms后处理的数据时，未指定该算子的attr属性N，导致输入数据不符合算子规范要求。

## 解决方案
在调用YoloV5DetectionOutput算子时，显式添加参数N=13，以适配nms后处理过的数据格式。

