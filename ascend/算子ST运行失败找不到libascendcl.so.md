# 算子ST运行失败找不到libascendcl.so

## 内核版本


## 问题现象
在MindStudio上运行算子ST测试时失败，提示“error while loading shared libraries: libascendcl.so: cannot open shared object file: No such file or directory”；或者编译时报错“/usr/bin/ld: cannot find -lascendcl”，表示系统无法找到libascendcl.so库文件。

## 问题根因
生成算子ST的测试代码在编译时需要链接libascendcl.so库，但运行时未正确指定该库的路径，导致系统无法加载该共享库。

## 解决方案
1. 搜索libascendcl.so库的实际路径（例如：/usr/local/Ascend/ascend-toolkit/latest/lib64）；2. 在MindStudio的ST配置界面中设置环境变量LD_LIBRARY_PATH指向该路径；3. （可选）将export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/lib64:${LD_LIBRARY_PATH}加入~/.bashrc以永久生效；4. 若仍报错，检查CMakeLists.txt等编译配置中是否正确导入LIB_PATH环境变量，必要时将$ENV{LIB_PATH}替换为实际路径。

