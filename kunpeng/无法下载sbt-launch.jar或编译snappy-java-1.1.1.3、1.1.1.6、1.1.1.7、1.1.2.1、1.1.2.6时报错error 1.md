# 无法下载sbt-launch.jar或编译snappy-java-1.1.1.3、1.1.1.6、1.1.1.7、1.1.2.1、1.1.2.6时报错error 1

## 内核版本


## 问题现象
执行编译时提示错误：make: *** [target/snappy-java-1.1.1.3.jar] Error 1。

## 问题根因


## 解决方案
1. 进入“/root/.sbt/launchers/0.13.5”目录；2. 在当前目录手动下载JAR包：wget https://scala.jfrog.io/ui/native/ivy-releases/org.scala-sbt/sbt-launch/0.13.5/sbt-launch.jar；3. 注释掉源代码目录下sbt文件中的该行代码：-sbt-launch-repo) require_arg path "$1" "$2" && sbt_launch_repo="$2" && shift 2 ;;

