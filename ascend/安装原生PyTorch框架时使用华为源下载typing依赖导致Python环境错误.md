# 安装原生PyTorch框架时使用华为源下载typing依赖导致Python环境错误

## 内核版本


## 问题现象
在pip设置为华为源时，安装requirements.txt中的typing依赖后，会导致Python环境错误。

## 问题根因
覆盖了Python原有的typing依赖，导致环境异常。

## 解决方案
在pip设置为华为源时，需打开requirements.txt文件，删除typing依赖，再执行命令：vi requirements.txt（进入文件删除typing依赖），然后运行pip3 install -r requirements.txt重新安装依赖列表。

