
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