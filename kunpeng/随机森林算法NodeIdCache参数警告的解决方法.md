# 随机森林算法NodeIdCache参数警告的解决方法

## 内核版本


## 问题现象
运行随机森林算法时，日志中出现ERROR级别的错误信息："<KunpengAlgorithmLibrary> MultiC and NodeIdCache are not supported at the same time!"

## 问题根因
加速库中的随机森林算法不支持开源MLlib中提供的NodeIdCache参数。

## 解决方案
建议将随机森林的NodeIdCache参数设置为false，该ERROR警告就会消失。若用户不希望修改代码，也可忽略此错误，加速库会自动将NodeIdCache设置为false，仍可以正常运行。

