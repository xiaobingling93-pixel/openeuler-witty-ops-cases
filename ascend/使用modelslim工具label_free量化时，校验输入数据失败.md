# 使用modelslim工具label_free量化时，校验输入数据失败

## 内核版本


## 问题现象
使用modelslim工具进行label_free量化时，校验输入数据失败，所有数据都无法被识别。

## 问题根因
输入数据calib_data格式有误，可能未满足双层list结构或数据非numpy格式。

## 解决方案
确保calib_data为双层list结构，并且内部数据为numpy格式。示例代码中通过将torch张量转换为numpy数组并包装成双层list（[[...]]）解决了问题。

