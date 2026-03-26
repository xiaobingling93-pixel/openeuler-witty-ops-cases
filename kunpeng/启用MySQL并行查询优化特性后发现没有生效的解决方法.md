# 启用MySQL并行查询优化特性后发现没有生效的解决方法

## 内核版本


## 问题现象
用户通过设置global参数方式启用MySQL并行查询优化特性（set global force_parallel_execute=on; set global parallel_default_dop=4;），但在当前连接中查询该特性的启用状态时发现没有生效。

## 问题根因
MySQL并行查询优化特性通过设置global参数的方式仅对新建立的连接生效，而不会影响当前已存在的会话连接。用户在设置global参数后未创建新连接，直接在当前会话中验证，因此看起来特性未生效。

## 解决方案
根据业务场景选择合适的设置方式：若需在当前连接生效，应使用session参数（set session force_parallel_execute=on; set session parallel_default_dop=4;）；若已使用global参数，则需新建数据库连接后再验证特性是否启用。

