# ModelArts上多机多卡运行GPT2-13B时报错Inconsistent batch shapes, batch operation expects same shape for each data row

## 内核版本


## 问题现象
在ModelArts上使用多机多卡训练GPT2-13B模型时，出现RuntimeError: Unexpected error. Inconsistent batch shapes, batch operation expects same shape for each data row, but got inconsistent shape in column 0, expected shape for this column is:<1025>, got shape:<1024>。

## 问题根因
问题根因可能是训练数据集制作时shape不匹配，或者数据集路径未正确传入。具体而言，训练数据处理时长度应等于模型接收长度加一，若不符合该要求会导致batch shape不一致；此外，在ModelArts上若未正确指定train数据集目录而非文件路径，也可能引发此错误。

## 解决方案
解决措施包括：1）按照文档重新制作数据集，确保训练数据处理时的长度等于模型接收长度加一；2）在ModelArts上正确指定train数据集的目录路径，而非本地文件路径。

