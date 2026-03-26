# 客户端安装Httpress，提示libev.so.4() (64bit) is needed by httpress-1.1.0.2.el7.x86_64的解决方法

## 内核版本


## 问题现象
安装HTTPress时，提示“libev.so.4() (64bit) is needed by httpress-1.1.0.2.el7.x86_64”。

## 问题根因
安装HTTPress需要libev.so.4依赖库，而该库未在系统中安装。libev.so.4（64bit）的包只能从EPEL源（Extra Packages for Enterprise Linux）获取。

## 解决方案
1. 下载libev的RPM包。
2. 将下载的RPM包上传到服务器中。
3. 安装libev.so.4（64bit）：
   ```
   rpm -ivh libev-4.15-3.el7.aarch64.rpm
   ```
4. 重新安装HTTPress：
   ```
   rpm -ivh httpress-1.1.0-2.el7.x86_64.rpm
   ```

