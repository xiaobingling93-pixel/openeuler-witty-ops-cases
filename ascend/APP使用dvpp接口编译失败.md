# APP使用dvpp接口编译失败

## 内核版本


## 问题现象
编译提示DVPP的相关接口未定义，编译报错，日志关键字包括：undefined reference to ***。

## 问题根因
DVPP与AscendCL已经分别打包到libacl_dvpp.so与libascendcl.so，测试用例使用了DVPP的相关接口，但没有链接libacl_dvpp.so。

## 解决方案
排查测试用例是否使用了预处理的接口但未链接libacl_dvpp.so。如果未链接，需要在编译文件中链接libacl_dvpp.so。具体需检查CMakeLists中的target_link_libraries()选项是否连接了acl_dvpp这个target，例如：target_link_libraries(main ascendcl acl_dvpp stdc++)。

