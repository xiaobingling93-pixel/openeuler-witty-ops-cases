# 在Windows系统环境下创建训练样例工程时报错“Unzip failed. There is probleam occurred when unzipping file.”

## 内核版本


## 问题现象
在Windows系统环境下使用MindStudio创建训练样例工程时，弹出错误提示：“Unzip failed. There is probleam occurred when unzipping file.”

## 问题根因
环境变量TMP指向的目录（通常是用户目录）可能因权限不足或路径问题导致解压失败。

## 解决方案
修改环境变量TMP，将其指向一个非用户目录下且具有读写权限的目录，例如D:\temp。

