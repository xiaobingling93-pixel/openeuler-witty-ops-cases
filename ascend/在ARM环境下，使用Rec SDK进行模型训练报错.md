# 在ARM环境下，使用Rec SDK进行模型训练报错

## 内核版本


## 问题现象
在ARM环境下，使用Rec SDK进行模型训练并且导入了scikit-learn库时存在报错：ImportError: /usr/local/python3.7.5/lib/python3.7/site-packages/sklearn/__check_build/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block。

## 问题根因
Rec SDK编译使用了OpenMP，OpenMP将使用ThreadLocalStorage（动态TLS）内存空间，sklearn在执行一些并行计算的时候需要使用静态TLS空间。在aarch64架构的机器上动态TLS和静态TLS使用的是相同的预分配池，先导入Rec SDK时导致预分配过多的内存空间，导致sklearn导入时libgomp.so空间不足。

## 解决方案
在模型代码中的main.py文件中将 import sklearn 置于导入Rec SDK之前，保证libgomp.so有足够的静态TLS空间。

