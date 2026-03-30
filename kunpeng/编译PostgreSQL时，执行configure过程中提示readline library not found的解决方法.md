# 编译PostgreSQL时，执行configure过程中提示readline library not found的解决方法

## 内核版本


## 问题现象
在编译PostgreSQL时，执行configure过程中提示“configure: error: readline library not found”。

## 问题根因
系统缺少readline动态库导致的问题。

## 解决方案
方案一（推荐）：安装readline相关依赖。步骤包括：1. 检查是否已安装readline（rpm -qa | grep readline）；2. 搜索readline相关包（yum search readline）；3. 安装readline-devel依赖包（yum -y install readline-devel）；4. 验证安装（rpm -qa | grep readline）；5. 返回PostgreSQL编译路径重新执行configure。方案二：执行configure时增加--without-readline参数（./configure --without-readline），但不建议使用此方法，因为readline用于命令行输入编辑功能。

