# 编译Gradle时提示Connection refused的解决办法

## 内核版本


## 问题现象
编译Gradle时提示Connection refused。

## 问题根因
尝试建立的连接被远程服务器或本地服务拒绝。

## 解决方案
创建一个名为build.sh的脚本，内容为循环执行./gradlew命令直到成功为止。具体步骤：1. 使用vim创建build.sh；2. 输入脚本内容（./gradlew; while [ $? -ne 0 ]; do sleep 3; ./gradlew; done）；3. 保存并退出；4. 执行sh build.sh运行脚本。

