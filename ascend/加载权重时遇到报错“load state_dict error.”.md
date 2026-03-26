# 加载权重时遇到报错“load state_dict error.”

## 内核版本


## 问题现象
在加载模型权重时出现RuntimeError，提示“Error(s) in loading state_dict for ShuffleNetV2: Missing keys in state_dict”，表明state_dict中缺少某些键。

## 问题根因
模型训练后保存的state_dict的key值与加载时的key值不一致，保存时在每个key前增加了'module.'前缀，导致加载时无法匹配原始模型结构。

## 解决方案
加载权重时遍历原始state_dict，将每个key去掉前7个字符（即'module.'前缀），构建新的字典后再调用model.load_state_dict()。示例代码：ckpt = torch.load("checkpoint.pth", map_location=loc); state_dict_old = ckpt['state_dict']; state_dict = {}; for key, value in state_dict_old.items(): key = key[7:]; state_dict[key] = value; model.load_state_dict(state_dict)

