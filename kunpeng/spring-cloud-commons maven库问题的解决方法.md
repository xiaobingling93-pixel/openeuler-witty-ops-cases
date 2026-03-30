# spring-cloud-commons maven库问题的解决方法

## 内核版本


## 问题现象
如果编译环境需要通过代理访问外部网络，则在编译时可能会遇到依赖拉取不到的问题，导致测试失败。错误信息示例：[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.1:test (default-test) on project spring-cloud-test-support: There are test failures.

## 问题根因
编译环境需要通过代理访问外部网络，而源码中硬编码的Maven中央仓库地址（https://repo.maven.apache.org/maven2）未配置代理或无法直接访问。

## 解决方案
提供两种解决方案：方法一：配置代理。编辑ModifiedClassPathRunner.java文件，在第42行下添加"import org.eclipse.aether.repository.Proxy;"，注释掉第222-224行，并在第225-230行添加使用代理的RemoteRepository配置，其中代理地址和端口（如127.0.0.1:3128）需根据实际环境修改，然后重新执行编译命令"mvn clean install -Dgpg.skip=true"。方法二：将源码中硬编码的Maven库地址替换为华为鲲鹏Maven仓库。注释第223行，在第224行新增"https://mirrors.huaweicloud.com/maven"，并在/etc/hosts中添加"172.30.163.193 mirrors.huaweicloud.com"，然后重新执行编译命令"mvn clean install -Dgpg.skip=true"。

