
# 第九讲_图像生成 Image Captioning

- 生成式对抗网络 Generative Adversarial network
![](https://i.imgur.com/klyAgcN.png)

- 学习数据分布：概率密度函数估计+数据样本生成
- 生成式模型是共生关系，判别式模型是因果关系
- GAN在生成模型的位置
![](https://i.imgur.com/Jm3WKO3.png)
- GAN特点
![](https://i.imgur.com/NJDn6A3.png)

## GAN

- 无监督网络框架
- 生成器generator and 判别器 discriminator
- 先学习判别器，然后固定判别器，优化生成器

### 生成器网络

- 生成样本数据
![](https://i.imgur.com/TRgCzPv.png)

### 判别器网络

- 样本有真实采样数据+生成器生成的样本数据
![](https://i.imgur.com/RJSAkZ5.png)

- EM优化是同方向优化，GAN最大最小优化

### 优化目标

- 价值函数
- 判别器价值函数最大化，生成器价值函数最小化；相反方向优化，对抗形式
- 纳什均衡点
- D（x）->1，D(G(x))->0，判别器的希望的；D(G(x))->1,生成器希望的
![](https://i.imgur.com/khjVXSZ.png)

#### 代价函数

- 改动最多的是G代价函数
![](https://i.imgur.com/QWIWse8.png)
![](https://i.imgur.com/UWEC5KS.png)
![](https://i.imgur.com/G9Acq2o.png)
- 三种游戏代价函数对比
- 生成器就是让判别器判别为真；需要的梯度回传是要学习判别为假的部分数据
![](https://i.imgur.com/Wgjblh4.png)

### 训练算法

- 训练
![](https://i.imgur.com/Q4PDOM4.png)
![](https://i.imgur.com/t3qhKAv.png)

- 问题和挑战
- 优化控制，很难达到纳什均衡
![](https://i.imgur.com/fTjI8gF.png)

## DCGAN图片生成

- 生成器
- 4个转置卷积
![](https://i.imgur.com/vS6qFOp.png)
- 重要的使用批归一化
![](https://i.imgur.com/huPut2P.png)
- 生成效果：仅支持低分辨率图片，无法捕捉物体结构
- Z向量的计算特征，插值特性

### 语义描述-->图片生成

- caption to image
![](https://i.imgur.com/ejhdbMS.png)

## 超分辨Super-Resolution

- 模型
![](https://i.imgur.com/nz3eht4.png)
- 两种代价函数
- 生成器的权重初始化，使用预训练的；训练才能成功
- 捕捉人类视觉感知代价-SRGAN
![](https://i.imgur.com/4I97ciN.png)

## 语义分割semantic segmentation

- 在原来的分割网络添加对抗生成器
- 添加对抗损失函数
![](https://i.imur.com/9DmiWmD.png)
- 降低模型过拟合

## SRGAN代码实现

- [https://github.com/349zzjau/ChinaHadoop_C9](https://github.com/349zzjau/ChinaHadoop_C9)
- 使用mnist数据集
- sugartensor库