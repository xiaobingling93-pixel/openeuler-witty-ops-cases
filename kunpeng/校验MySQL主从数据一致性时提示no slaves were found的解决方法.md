# 校验MySQL主从数据一致性时提示no slaves were found的解决方法

## 内核版本


## 问题现象
校验MySQL主从数据一致性时提示“no slaves were found”。

## 问题根因
主库无法获取从库的IP地址信息，因为主库执行show slave hosts命令时依赖从库配置中的report-host参数，而该参数未设置。

## 解决方案
1. 登录主库执行show slave hosts;发现Host为空。
2. 确认主从数据一致后，先关闭从库，再关闭主库。
3. 在主库和从库的my.cnf配置文件中分别添加report_host=对应IP（根据实际IP填写）。
4. 保存配置并退出。
5. 先启动主库，再启动从库，确认主从复制建立成功。
6. 再次在主库执行show slave hosts;，Host字段将显示从库IP地址。

