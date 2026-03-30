# 升级Faiss后，IVFSQ算法train和add接口性能下降

## 内核版本


## 问题现象
从Faiss 1.7.1版本升级到Faiss 1.7.4版本后，在设置useKmeansPP为false的情况下，IVFSQ算法的train和add接口性能下降。

## 问题根因
在useKmeansPP为false时，IVFSQ算法使用IndexFlat进行CPU聚类。Faiss 1.7.1版本中使用了带omp加速的HeapResultHandler::add_results接口，而1.7.4版本改用新增的SingleBestResultHandler::add_results接口，该接口未使用omp加速，导致性能下降。

## 解决方案
在Faiss源码的SingleBestResultHandler::add_results接口中添加omp并重新编译安装，以恢复性能加速。

