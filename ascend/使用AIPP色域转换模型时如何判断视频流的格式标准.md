# 使用AIPP色域转换模型时如何判断视频流的格式标准

## 内核版本


## 问题现象
使用AIPP色域转换模型时无法判断视频流的格式标准。

## 问题根因
AIPP中色域转换要求视频流格式为BT-709WIDE、BT-709NARROW、BT-601WIDE等，但用户通常无法确定一段视频流属于哪种格式，从而难以选择正确的色域转换模板。

## 解决方案
使用第三方ffprobe工具判断视频流格式：1. 从https://www.ffmpeg.org/ffprobe-all.html下载ffprobe工具；2. 执行命令 ffprobe -show_frames filename 获取视频帧信息；3. 根据输出中的 color_range（tv 表示 narrow range，pc 表示 wide range）和 color_space（bt709 或 bt601）字段确定视频标准。例如，color_range=tv 且 color_space=bt709 对应 BT-709 NARROW。

