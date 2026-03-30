# pip3 install报错“subprocess.CalledProcessError：Command '('lsb_release', '-a')' return non-zero exit status 1”

## 内核版本


## 问题现象
在使用pip3 install命令安装软件包时，出现错误：subprocess.CalledProcessError: Command '('lsb_release', '-a')' returned non-zero exit status 1。

## 问题根因
用户自行编译安装的Python 3.7.5在执行subprocess模块调用lsb_release -a时，无法找到lsb_release.py模块。因为该Python环境的lib路径（/usr/local/python3.7.5/lib/python3.7/）下缺少lsb_release.py文件，导致命令执行失败。

## 解决方案
1. 使用find / -name lsb_release命令查找系统中是否存在lsb_release可执行文件（通常位于/usr/bin/lsb_release）；2. 将找到的/usr/bin/lsb_release文件备份（如mv /usr/bin/lsb_release /usr/bin/lsb_release.bak）；3. 再次执行pip3 list验证问题是否解决。

