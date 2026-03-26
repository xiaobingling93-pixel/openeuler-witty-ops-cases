# 将数据导入MySQL时提示时区问题的解决方法

## 内核版本


## 问题现象
将数据导入MySQL时出现错误：ERROR: The server time zone value 'EDT' is unrecognized or represents more than one time zone. You must configure either the server or JDBC driver (via the serverTimezone configuration property) to use a more specific time zone value if you want to utilize time zone support.

## 问题根因
MySQL服务器无法识别JDBC driver的默认时区“EDT”，需要指定JDBC driver使用更明确的时区（如UTC或MySQL服务器的时区）。

## 解决方案
在my_mysql.properties文件的jdbc配置中添加参数serverTimezone=UTC，保存后重新执行数据加载命令。具体步骤：1. 打开my_mysql.properties文件；2. 在jdbc配置行添加serverTimezone=UTC；3. 保存并退出；4. 重新运行./runDatabaseBuild.sh my_mysql.properties。

