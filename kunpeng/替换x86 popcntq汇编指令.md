# 替换x86 popcntq汇编指令

## 内核版本


## 问题现象
编译报错：Error: unknown mnemonic 'popcnt' -- 'popcnt [sp,8],x0'。

## 问题根因
popcnt为x86平台的位1计数指令，鲲鹏平台无对应指令，需使用替换算法实现。

## 解决方案
在鲲鹏平台上使用ARM NEON指令替代x86的popcnt指令。具体实现方式为：包含<arm_neon.h>头文件，通过vcnt_u8、vpaddl_u8、vpaddl_u16、vpaddl_u32等NEON指令对输入数据逐级累加计算位1的个数，最终返回结果。示例代码如下：
#include <arm_neon.h>
static inline uint64_t POPCNT_popcnt_u64(uint64_t x)
{ 
    uint64_t count_result = 0; 
    uint64_t count[1]; 
    uint8x8_t input_val, count8x8_val; 
    uint16x4_t count16x4_val; 
    uint32x2_t count32x2_val; 
    uint64x1_t count64x1_val; 
    input_val = vld1_u8((unsigned char *) &x); 
    count8x8_val = vcnt_u8(input_val); 
    count16x4_val = vpaddl_u8(count8x8_val); 
    count32x2_val = vpaddl_u16(count16x4_val); 
    count64x1_val = vpaddl_u32(count32x2_val); 
    vst1_u64(count, count64x1_val); 
    count_result=count[0]; 
    return count_result; 
}

