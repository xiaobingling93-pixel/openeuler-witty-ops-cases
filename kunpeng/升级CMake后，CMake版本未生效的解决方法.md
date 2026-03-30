# 升级CMake后，CMake版本未生效的解决方法

## 内核版本


## 问题现象
执行升级CMake操作后，查看CMake版本，发现版本未生效。

## 问题根因
环境中存在其它CMake版本，优先级比编译安装的CMake版本高。

## 解决方案
1. 使用命令 find / -name cmake | grep bin 查看环境中所有的CMake路径；2. 分别检查如 /usr/local/bin/cmake 和 /usr/local/cmake/bin/cmake 的版本；3. 通过以下步骤使新编译安装的CMake生效：进入 /usr/local/bin/ 目录，将旧 cmake 重命名为 cmake-3.18.2（示例版本），然后执行 hash -r 清除shell缓存，最后验证 cmake --version。

