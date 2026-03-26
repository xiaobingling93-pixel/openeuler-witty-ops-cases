# spring-cloud-function依赖拉取问题的解决方法

## 内核版本


## 问题现象
如果编译环境使用代理访问外部网络，可能会遇到依赖拉取失败的问题。

## 问题根因
编译环境需要通过代理访问外部网络，但spring-cloud-function的DependencyResolver未正确配置代理或默认Maven仓库不可达。

## 解决方案
提供两种解决方案：方法一：配置代理。修改DependencyResolver.java文件，添加Proxy导入并设置代理地址和端口；同时修改RuntimeJavaCompilerTests.java文件中的方法名。方法二：将Maven库替换为华为Maven库。修改DependencyResolver.java指向华为鲲鹏Maven仓库，在/etc/hosts中添加对应IP，并为spring-cloud-function-deployer模块的settings.xml配置代理信息。最后重新执行编译命令 ./mvnw clean install -Dgpg.skip=true。

