# Storm+Kafka某个测试用例测试完成后未自动删除相应产生的topic

## 内核版本


## 问题现象
Storm+Kafka某个测试用例测试完成后未自动删除相应产生的topic。

## 问题根因


## 解决方案
手动删除该用例产生的topic。具体操作包括：首先使用`storm list`查看运行的拓扑，然后使用`storm kill wordcount`终止对应的拓扑；接着设置ZooKeeper连接地址（如zklist=DataNode1:24002,DataNode2:24002,DataNode3:24002），最后执行`kafka-topics.sh --zookeeper $zklist:24002/kafka --delete --topic testTopic`命令删除对应的Kafka topic。

