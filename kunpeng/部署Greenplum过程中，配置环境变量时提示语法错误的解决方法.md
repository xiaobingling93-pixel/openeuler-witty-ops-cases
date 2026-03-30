# 部署Greenplum过程中，配置环境变量时提示语法错误的解决方法

## 内核版本


## 问题现象
部署Greenplum过程中，在配置环境变量时提示“-bash:/root/.shell/shared_func:line195...”语法错误。

## 问题根因
配置环境变量时存在语法错误，具体表现为/root/.shell/shared_func和/root/.shell/shared_alias文件中函数定义格式不正确（如缺少括号等）。

## 解决方案
1. 修改/root/.shell/shared_func文件第192行为"ai2(){"；2. 修改/root/.shell/shared_alias文件第142行为"ai2(){"；3. 执行"source /home/gpadmin/.bash_profile"使配置生效；4. 修改/root/.shell/shared_func文件第216行为"ad2(){"；5. 修改/root/.shell/shared_alias文件第160行为"ad2(){"；6. 再次执行"source /home/gpadmin/.bash_profile"；7. 修改/root/.shell/shared_func文件第220行为"dL2(){"；8. 修改/root/.shell/shared_alias文件第164行为"dL2(){"；9. 最后再次执行"source /home/gpadmin/.bash_profile"使所有修改生效。

