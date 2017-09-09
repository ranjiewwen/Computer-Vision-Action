
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

![](https://i.imgur.com/dljAU07.png)