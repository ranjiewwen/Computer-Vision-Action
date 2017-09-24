
# 第七讲_图像描述（图说）Image Captioning

- 本章结构
![](https://i.imgur.com/hPDPYkb.png)
- 递归神经网络
![](https://i.imgur.com/FkcEB8H.png)

- 时序后向传播（BPTT）
![](https://i.imgur.com/ySa3BWd.png)

## 朴素Vanilla-RNN

- 基本模型
- 用sigmoid存在严重的梯度消失
![](https://i.imgur.com/vPqQ1CZ.png)

## LSTM长短时记忆模型（97年提出）

- 基本模型
![](https://i.imgur.com/dF7xArG.png)
- 模型对比
![](https://i.imgur.com/vNwn6z7.png)
- LSTM数学模型
![](https://i.imgur.com/21W6b3d.png)
- 控制门作用理解
- LSTM结构图
![](https://i.imgur.com/TA1lRzN.png)
![](https://i.imgur.com/xotpRqr.png)
![](https://i.imgur.com/lxkwpIb.png)
![](https://i.imgur.com/kH6joNr.png)
![](https://i.imgur.com/GyVWr0Y.png)
![](https://i.imgur.com/lMkbj9v.png)
![](https://i.imgur.com/080maoq.png)

- LSTM变种：
- Peephole
- Coupled 忘记输入门

## GRU门限递归单元（Gated Recurrent Unit）

- 改进
![](https://i.imgur.com/7xVN07y.png)
- LSTM和GRU比较
![](https://i.imgur.com/EMZANfb.png)

## 图像描述

- 为图片生成描述语言
![](https://i.imgur.com/1nXOA84.png)

- 具有多模态理解和推理；复合理解与推理等研究难点和挑战
![](https://i.imgur.com/LGQ7Psm.png)
- 传统的分段处理策略
![](https://i.imgur.com/Hb4W5Ke.png)
- 新的点对点策略
![](https://i.imgur.com/C2SQdLw.png)
- 模型组成
![](https://i.imgur.com/9jXMpgG.png)

## Show and tell 模型

- 概述
![](https://i.imgur.com/xqlk5U8.png)
![](https://i.imgur.com/eIHkgHk.png)

- 具有attention机制模型
![](https://i.imgur.com/I6hYXMy.png)
![](https://i.imgur.com/jtipXQG.png)

### 数据集

- MSCOCO标注集
![](https://i.imgur.com/Xw0CvFK.png)