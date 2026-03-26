# 使用Atlas 推理系列产品时，JPEG图片解码失败

## 内核版本


## 问题现象
在使用Atlas推理系列产品的DVPP模块进行JPEG图片解码时失败，日志报错信息包括：'just support jpeg with YUV 444 422 420 400'、'do not support progressive mode'、'do not support arithmetic code, support huffman code only'，以及'EOI segment of the stream is invalid'。

## 问题根因
JPEG解码失败的原因主要有两个：一是输入的JPEG图片格式不被支持，例如使用了算术编码、渐进编码、JPEG2000格式，或颜色采样格式不在YUV 444/422/420/400范围内；二是图像数据不完整，例如缺少JPEG标准结束标记FF D9（EOI），或在传输过程中数据损坏导致码流与原始图像不一致。

## 解决方案
1. 对于不支持的JPEG格式，建议使用第三方软件预先解码后再输入；2. 若报错提示EOI无效，应检查原始图像二进制数据是否以FF D9结尾，若缺失则需更换完整图像；3. 若原始图像完整但解码仍失败，应在调用acldvppJpegDecodeAsync前通过fwrite保存传入的码流，并与原图进行二进制比对，若不一致则需排查数据传输过程中的损坏问题。

