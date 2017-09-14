
# 第四讲_图像识别之图像分类Image Classification

- 目录
![](https://i.imgur.com/BHIBc3U.png)

## 图片分类

- 性能指标：top1,top5
- ILSVRC：每种任务数据集不一样
![](https://i.imgur.com/h1lHmby.png)
- imageNet：根据WorldNet组织的图片集，为每个名词提供平均1000张图片
- 网络进化
![](https://i.imgur.com/RsXDsbC.png)
![](https://i.imgur.com/2hHVXg8.png)

## 卷积神经网络（CNN）

- 基础神经网络：
> - 神经元（输入，w,b,sigmoid）
> - 优化：梯度下降，BP反向传播（链式规则），3~5层
> - 优化交叉熵（之前是均方误差）：批量梯度下降，随机梯度下降（学习率、步长，扰动->动量算法momentum）

- 构建CNN的基本层

### 卷积层

- 不同的损失函数：注意跳出**鞍点**（在一个方向极小值，另一个方向极大值）
![](https://i.imgur.com/uYgYVOs.png)
![](https://i.imgur.com/tJVfr65.png)
![](https://i.imgur.com/OBD0fH8.png)
- ReLU激活函数：分段线性函数，无饱和问题，明显减轻梯度消失问题
- **卷积步长大于1，有降维的作用**

### 池化层
- 特征融合，降维
![](https://i.imgur.com/dljAU07.png)

### 全连接层
![](https://i.imgur.com/R2bPlRS.png)

### Softmax层
![](https://i.imgur.com/jMN6gqC.png)

## 工程实际

![](https://i.imgur.com/VimT7dw.png)

## AlexNet

- 基本概述
![](https://i.imgur.com/7oQyh3h.png)
- 局部响应归一化
![](https://i.imgur.com/GNYk5py.png)
![](https://i.imgur.com/rQpVNx9.png)

## Network-in-Network(NiN)

- 1*1卷积层，实现特征的降维，这个就是卷积核的大小
![](https://i.imgur.com/10B7AxW.png)

## VGG网络-2014

- 卷积核的分解
![](https://i.imgur.com/px0RIo1.png)
- **由于最后的卷积层--->第一个全连接；就是需要全局卷积，这里的卷积核大小是超参数，是固定的参数，所以对输入图片的大小有要求；而ResNet对输入图片大小没有要求**
- 网络结构，D,E结构用的多一些
![](https://i.imgur.com/v80RTYu.png)

## GoogLeNet网络

- 进化顺序
![](https://i.imgur.com/73diBd6.png)
- **Inception V1网络**
- 和ResNet一样有基本的模块
![](https://i.imgur.com/wOUbh4e.png)
![](https://i.imgur.com/9VMcYYt.png)
- 取消全连接层；最后的卷积层--->第一个全连接需要的参数最多
![](https://i.imgur.com/vgrEqAB.png)
- 网络结构
![](https://i.imgur.com/6aZ09Tc.png)
- 网络参数
![](https://i.imgur.com/uOkd7tM.png)
- 两个辅助分类器：深度网络中，梯度回传到最初层，严重消失；有效加速收敛，**测试阶段不使用**

## Inception V2网络

- 核心有批归一化
- 一批一批batch进行处理，每一批在第k个通道进行均值方差归一化操作
![](https://i.imgur.com/9Oyl0Bz.png)
![](https://i.imgur.com/GJYFLhP.png)
![](https://i.imgur.com/Byodnfo.png)

## Inception V3网络

- 卷积进行分解：非对称卷积；三种分解方案
![](https://i.imgur.com/aI1OKqA.png)

- 高效的降尺寸：避免表达瓶颈
![](https://i.imgur.com/4apUceo.png)
![](https://i.imgur.com/XqKVgmY.png)
- 网络整体框架
![](https://i.imgur.com/JNOIEQn.png)

## ResNet残差网络

- skip/shortcut connection
![](https://i.imgur.com/FBKEJbV.png)
- 虚线有降维作用
![](https://i.imgur.com/6hUr4Jb.png)
- 往更深的走
- 原始输入改为256，优化就是先通道降维，然后卷积，升维
![](https://i.imgur.com/efUHIjQ.png)
- 网络整体情况：5个卷积组
![](https://i.imgur.com/57OGYTn.png)

## Inception V4网络

- 引入残差
![](https://i.imgur.com/LuJtAji.png)

## ResNeXt网络

- 概况
![](https://i.imgur.com/MSTBvGB.png)
- 1**1卷积就相当于全连接降通道数
- 32**4d块，保证参数量不变；32*4=128通道是普通64通道的2倍
- 分支数就是基数，网络宽度就是分支数*每个分支的通道数
![](https://i.imgur.com/mUFlYv1.png)
![](https://i.imgur.com/LzoSiPM.png)

## CNN设计准则

- 避免信息瓶颈：数据量H**W(尺度大小)*C(通道数)变换要缓慢；通道数要不能弥补尺度减小，但要缓慢

- 通道（卷积核）数量保持在可控范围内

- 感受野要足够大
![](https://i.imgur.com/xztlGto.png)

- 分组策略--降低计算量
- 低秩分解
![](https://i.imgur.com/E40a5Tx.png)

## 实验结果

- 代码实验ResNet