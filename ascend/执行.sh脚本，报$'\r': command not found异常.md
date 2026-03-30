# 执行.sh脚本，报$'\r': command not found异常

## 内核版本


## 问题现象
在Linux系统中执行.sh脚本时，报错：$'\r': command not found。

## 问题根因
该.sh脚本是在Windows系统下编写或编辑的，其换行符为\r\n，而Linux系统仅识别\n作为换行符。当脚本中包含Windows风格的换行符\r时，Linux会将其误认为是一个命令，从而导致“$'\r': command not found”错误。

## 解决方案
在Linux系统中执行命令 sed -i 's/\r//' *.sh，以删除.sh脚本中的\r字符，将换行符统一为Linux格式。

