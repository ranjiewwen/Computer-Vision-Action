# 第二讲_图像数据处理Image Data Processing

- 深度模型出现后被弱化，但是思想的影子在深度模型中可以看到的

## 图片存储原理

- RGB颜色空间:三通道（b,g,r），加法混色
- CMY(K):减法混色，用到印刷中；四个通道（c,m,y,k）
- HSI/HSV颜色空间：基于人类视觉；
![](https://i.imgur.com/POL1szc.png)
- CIE-XYZ颜色空间：国际照明协会，人类视觉系统-视锥细胞：主要有短，中，长波段
- CIE-Lab对色空间
![](https://i.imgur.com/VnWnuf0.png)
- 单通道灰度图：Gray=R*0.3+G*0.59+B*0.11,转换公式灰度化

## 空域分析和变换

- 滤波和卷积
- 领域参数选择，模板参数设计
![](https://i.imgur.com/AiTpVz1.png)
- 边界补充方式：补零；边界复制(replication),镜像(reflection),块复制（wraparound）
- 平滑均值滤波/卷积
- 平滑中值滤波/卷积：有效出去椒盐噪声
- 平滑高斯滤波/卷积：离中心越近，权重越大
![](https://i.imgur.com/kG1W7cE.png)
- sigma越小，越集中中心区域
-深度模型改进时进行2D->1D降计算
![](https://i.imgur.com/QoFLEzP.png)
- 梯度Prewitt滤波/卷积
![](https://i.imgur.com/eb0F6aY.png)
- 梯度Sobel滤波/卷积
![](https://i.imgur.com/VJ8WHTn.png)
- 梯度Laplacian滤波/卷积
- 其中领域大小为超参数，需要实验确定
![](https://i.imgur.com/2eXZ04j.png)
- 锐化，LOG
- canny边缘检测算子实现
- [canny算子](http://blog.csdn.net/xiaojiegege123456/article/details/7714897)
> Canny边缘检测算法：
     step1:用高斯滤波器平滑图象；
     step2:用一阶偏导的有限差分来计算梯度的幅值和方向；
     step3:对梯度幅值进行非极大值抑制；
     step4:用双阈值算法检测和连接边缘。

## 频域分析及变换

### 傅里叶变换
- 滤波-除去特定频率和加速计算-时域卷积变为频域相乘
- 应用信号分解
- 离中心点越远，频率越高，越亮幅度越大
- 相位即梯度的方向，不同的相位方向表示不同的边缘轮廓
![](https://i.imgur.com/JyvVIDT.png)
- 空域卷积=频域相乘
![](https://i.imgur.com/YqL9FQq.png)
### 高斯金字塔

- 高斯卷积+降采样
![](https://i.imgur.com/aGFOVBM.png)
- 高斯金字塔的必要性，直接降采样损失信息
![](https://i.imgur.com/ywQUW8b.png)
- 尺度空间：不同尺度适合不同尺寸的物体，合适的尺度永远未知。

### 拉普拉斯字塔Laplacian

- 保留高频信息，用于图像恢复
![](https://i.imgur.com/jueqnhz.png)
- 左边Gaussian Pyramid由上向下；中间Laplacian Pyramid由下到上；右边图像是图像恢复
![](https://i.imgur.com/c98s487.png)

### 模板匹配

- 相似度量
![](https://i.imgur.com/RU61KOb.png)