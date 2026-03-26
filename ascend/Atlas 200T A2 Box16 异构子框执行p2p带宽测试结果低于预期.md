# Atlas 200T A2 Box16 异构子框执行p2p带宽测试结果低于预期

## 内核版本


## 问题现象
Atlas 200T A2 Box16 异构子框在执行p2p带宽测试时，出现无法执行指令并报错，或测试结果未达到预期。

## 问题根因
当前环境下开启了ACSCtl，可能影响了p2p带宽测试的结果。

## 解决方案
执行以下命令关闭ACSCtl：
for pdev in `lspci -vvv|grep -E "^[a-f]|^[0-9]|ACSCtl"|grep ACSCtl -B1|grep -E "^[a-f]|^[0-9]"|awk '{print $1}'` 
do
setpci -s $pdev ECAP_ACS+06.w=0000 
done

