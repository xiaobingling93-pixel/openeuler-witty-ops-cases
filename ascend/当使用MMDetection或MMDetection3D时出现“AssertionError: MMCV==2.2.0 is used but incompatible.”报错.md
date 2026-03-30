# 当使用MMDetection或MMDetection3D时出现“AssertionError: MMCV==2.2.0 is used but incompatible.”报错

## 内核版本


## 问题现象
当安装的MMDetection版本为3.2.0及以上，MMDetection3D版本为1.3.0及以上，且MMCV版本为2.2.0时，运行MMDetection或MMDetection3D会报错：AssertionError: MMCV==2.2.0 is used but incompatible. Please install mmcv>=2.0.0rc4, <2.2.0。

## 问题根因
mmdetection/mmdet/__init__.py和mmdetection3d/mmdet3d/__init__.py中限定mmcv_maximum_version = '2.2.0'，但断言检查要求当前安装的MMCV版本必须小于该值（<），导致版本号恰好为2.2.0时校验失败。

## 解决方案
修改MMDetection和MMDetection3D源码中的版本判断逻辑：将mmdetection/mmdet/__init__.py和mmdetection3d/mmdet3d/__init__.py中的'mmcv_version < digit_version(mmcv_maximum_version)'改为'mmcv_version <= digit_version(mmcv_maximum_version)'，以允许等于2.2.0的版本通过校验。

