# PyTorch框架利用imagenet2012训练resnet50报错“Couldn’t find any class”

## 内核版本


## 问题现象
PyTorch框架利用imagenet2012训练resnet50失败，报错“Couldn’t find any class folder in XXX”。

## 问题根因
数据集格式错误。训练和验证数据集未按照代码要求的目录结构组织：train目录下应为1000个类别子目录，每个子目录包含对应类别的图像；val目录也需通过脚本处理成相同结构，而原始解压后的数据不符合该格式。

## 解决方案
1. 制作符合要求的train数据集格式：解压ILSVRC2012_img_train.tar后得到1000个tar文件，编写并运行脚本将每个tar文件解压到以其类别命名的子目录中。2. 制作符合要求的val数据集格式：解压ILSVRC2012_img_val.tar后得到50000张图片，将val_prep.sh脚本放入val目录并运行，该脚本会根据ImageNet官方提供的标签信息将图片移动到对应的类别子目录中。

