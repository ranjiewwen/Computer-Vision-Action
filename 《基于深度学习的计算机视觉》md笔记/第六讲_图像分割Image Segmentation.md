# 第六讲_图像分割Image Segmentation

- 目录
![](https://i.imgur.com/Siii1wX.png)
- +三大数据库

### 显著性检测saliency detection

- 两类问题
![](https://i.imgur.com/Sf81mKr.png)
![](https://i.imgur.com/D2T5pNL.png)
- 数据集的标注
![](https://i.imgur.com/r4UH2n5.png)
- DNN网络：VGG改进而来，分割输出是和原图大小一样；实际该模型就是全卷积网络
![](https://i.imgur.com/yXgFhEr.png)

### 物体分割 object segmentation

- 前背景分割（前景包含物体，需要提供初始标记）
- Graph Cuts分割
![](https://i.imgur.com/kYJksEF.png)
- GrabCut分割:需要人工标记矩形框或者随意标记框
- 前景、背景的颜色模型
- opencv已经实现，效果不错
> - 高斯混合模型
> - Kmeans算法获得
- 算法流程
![](https://i.imgur.com/ls6uiCT.png)

### 语义分割 semantic segmentation

- 多类的分割
- 什么是语义分割，不需要事先标记分割
![](https://i.imgur.com/Qsnq3Y2.png)
- 用处：机器人视觉，自动驾驶，X光
- 算法研究阶段
![](https://i.imgur.com/S0qKrqu.png)

### 全卷积网络 Fully Convolution Network

- FCN（2015）--检测部分的区域R-FCN(2016)
- 解决低分辨率问题：反卷积
![](https://i.imgur.com/bj1fnhQ.png)
- 卷积化：全连接->1x1卷积
- 32倍降采样
![](https://i.imgur.com/lTJlyNF.png)

- FCN-反卷积
![](https://i.imgur.com/E4ldnQV.png)
- 输入输出分奇偶情况
- 反池化操作效果好的网络一般不用
- FCN的跳层结构skip-layer
![](https://i.imgur.com/dGqbaKN.png)
![](https://i.imgur.com/OVZ4HDp.png)
- FCN构架
![](https://i.imgur.com/3gwGUS2.png)
- 使用AlexNet构建FCN-32s-16s-8s网络
- FCN训练
![](https://i.imgur.com/mQIgDLV.png)
- FCN的跳层结构性能
![](https://i.imgur.com/o8Wk4ir.png)
- VGG-16效果最优
- FCN结果
![](https://i.imgur.com/vknnvrZ.png)
