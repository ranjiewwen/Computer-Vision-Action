
# 第三讲_图像特征与描述Image Feature Descriptor

- 概要
![](https://i.imgur.com/6S8BdQx.png)

## 特征提取方法

### 直方图

- 对图片数据/特征分布的一种统计；对不同量进行直方图统计；可以表示灰度，颜色，梯度，边缘，形状，纹理，局部特征等
- 灰度直方图；对量化的bin需要人工选择；量化过宽过窄都不好

### 聚类

- 混合样本集中内在群组关系
- 常用方法：Kmeans,EM算法，Mean Shift;谱聚类，层次聚类等
![](https://i.imgur.com/lpdrr7w.png)
- 贪心算法，经常陷入局部最优解（非全局最优）
- K值和初始中心点选择
![](https://i.imgur.com/oHHVULU.png)

## 颜色特征

- 量化颜色直方图：适用于RGB,HSV等均匀空间
- **聚类颜色直方图：适合Lab等非均匀空间；考虑对图像质量感知和图像恢复！**

## 几何特征

### 边缘

- 边缘edge:像素明显变换的区域，一阶导数的极值区域
- 先高斯去噪，再使用一阶导数获取极值；导数对噪声敏感。
- 高斯滤波sigma标准差代表物体的尺度
- 边缘提取尺度问题：不同标准差的滤波捕捉不同尺度的边缘
![](https://i.imgur.com/XWe9en6.png)

### 兴趣点/关键点（Interest point/keypoint）

- 不同视角图片之间的映射
- 稳定局部特征点,具有显著性，抗变形等
- 运用于图片配准，拼接；运动跟踪，物体识别，3D重建，机器人导航

### Harris 角点

- 显著点，在任何方向上移动小观察窗，导致大的像素变动
- 非极大值抑制
![](https://i.imgur.com/Wx8Dums.png)
![](https://i.imgur.com/dxau5ZO.png)

### 斑点（blob）

- 拉普拉斯梯度：一阶导数极值点，二阶导数零点，对噪声敏感，需要先做高斯平滑
- 二阶高斯导数滤波LoG
![](https://i.imgur.com/6a0QISS.png)

## 局部特征

### sift关键点

- 特点
![](https://i.imgur.com/7VeQt8T.png)

- scale-invariant feature transform
- 计算步骤
> - 计算高斯差分（DoG）尺度空间，获取极值点
- 特征点处理：位置插值，除去低对比度点，去除边缘点
- 方向估计，描述子提取

- 尺度空间通过sigma不同实现
![](https://i.imgur.com/sf4MkQd.png)
![](https://i.imgur.com/RO0J591.png)
- 圆半径：特征点尺度；圆心：特征点坐标
- 特征点估计
![](https://i.imgur.com/mu8zaWq.png)
- 特征点方向归一化：将坐标轴方向旋转为关键点方向（方向不变性）
- 特征点描述子：旋转后的坐标上采样16*16的像素窗，8方向直方图累计梯度幅度
![](https://i.imgur.com/J6PcXfj.png)

### Surf （Speeded up robust features）

- sift近似算法，实现快速版：主要有均值滤波和积分图像
- 加速，精度略有牺牲

### HOG

- 方向梯度直方图
![](https://i.imgur.com/ePcL4sA.png)
- 特征由来
![](https://i.imgur.com/lUFCgB5.png)

### LBP局部二只模式

- 基本已了解

### Gabor滤波器组

- 多方向和尺度
![](https://i.imgur.com/GB8vbPU.png)
![](https://i.imgur.com/cLJ30Xh.png)
