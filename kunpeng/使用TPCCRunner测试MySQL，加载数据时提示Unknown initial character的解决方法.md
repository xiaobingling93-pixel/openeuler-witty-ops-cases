# 使用TPCCRunner测试MySQL，加载数据时提示Unknown initial character的解决方法

## 内核版本


## 问题现象
使用TPCCRunner测试MySQL，在准备TPC-C测试环境并加载数据时，提示“Unknown initial character set index '255' received from server. Initial client character set can Exception in thread "main" java.lang.NullPointerException”。

## 问题根因
MySQL驱动和数据库字符集不一致导致的问题。

## 解决方案
需要修改“conf/example/mysql/loader.properties”文件，设置MySQL数据库连接使用Unicode字符集，并使用UTF-8编码方式进行数据传输。具体步骤：1. 打开“conf/example/mysql/loader.properties”文件；2. 在文件中添加“useUnicode=true&characterEncoding=utf8”；3. 重新加载数据。

