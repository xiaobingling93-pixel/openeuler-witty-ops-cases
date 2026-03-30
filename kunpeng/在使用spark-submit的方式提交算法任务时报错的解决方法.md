# 在使用spark-submit的方式提交算法任务时报错的解决方法

## 内核版本


## 问题现象
在使用spark-submit的方式提交随机森林、决策树、GBDT算法任务时，配置“spark.driver.userClassPathFirst=true”或“spark.executor.userClassPathFirst=true”，会导致算法异常终止，并报ClassCastException异常或loader constraint violation错误。

## 问题根因
这两个参数为实验参数，会改变Spark任务JAR包加载顺序，导致类冲突。

## 解决方案
在spark-submit提交任务时，去掉“spark.driver.userClassPathFirst=true”或“spark.executor.userClassPathFirst=true”配置。

