# 第五讲_图像识别之图像检测Image Detection

- 目录
![](https://i.imgur.com/wxLiGQf.png)

- 物体检测
![](https://i.imgur.com/FzMV4lg.png)
![](https://i.imgur.com/ggt7bEo.png)
- ILSVRC竞赛200类(每个图片多个标签)：输出类别+Bounding Box（x,y,w,h）
- PASCAL VOC 2012只有20类
![](https://i.imgur.com/RlTboWN.png)
- 模型进化
![](https://i.imgur.com/QdVeMNB.png)

## 区域卷积神经网络R-CNN-2014

- 模型结构
![](https://i.imgur.com/sWzqbLB.png)
- selective search+CNN特征+svm+Bounding box regression
![](https://i.imgur.com/nFNUBAB.png)
- Regiom proposals
- 训练流程
![](https://i.imgur.com/bXTzWoh.png)
![](https://i.imgur.com/6z20Lf2.png)
![](https://i.imgur.com/3zhxTIW.png)
- 测试阶段
![](https://i.imgur.com/UKdzcx7.png)
- RCNN性能大幅提升
![](https://i.imgur.com/5B93Jzu.png)

## SPPNet网络-2014

- R-CNN速度慢的重要原因：卷积特征重复计算量太大
![](https://i.imgur.com/ivKtrPu.png)
- spp技术实现了共享计算，适应不同输入尺寸
![](https://i.imgur.com/iE1D7Kh.png)
- SPP层具体实现
![](https://i.imgur.com/g4sWMAj.png)
- sppNet问题
![](https://i.imgur.com/DIopWBM.png)

## Fast-R-CNN-2015

- 改进；更高mAP(类似AUC曲线下的面积)
![](https://i.imgur.com/B0QG6jV.png)
- 网络结构
![](https://i.imgur.com/0kUxynw.png)
![](https://i.imgur.com/5qoXc8W.png)
![](https://i.imgur.com/8yIskW0.png)
![](https://i.imgur.com/PBelkwe.png)
- 训练阶段
![](https://i.imgur.com/jxDrL7u.png)

## Faster-R-CNN-2015

- 概况，引导CNN关注区域
![](https://i.imgur.com/pJEAaAs.png)
- Region Proposal Network
![](https://i.imgur.com/hLuS9BZ.png)
- 训练过程
![](https://i.imgur.com/DXUyJQn.png)

## 区域全卷积神经网络R-FCN

- 回顾
![](https://i.imgur.com/uOfiBfl.png)
- F-RCN的设计过程
- 分类问题对尺寸，方向等变换不敏感，网络越深，分类效果很好；但是检测对变换敏感
![](https://i.imgur.com/LmeL8Nk.png)
![](https://i.imgur.com/qpSSELa.png)
- 结构图：三部分
![](https://i.imgur.com/S7lxbvQ.png)
- 理解K2(C+1)个通道，映射到每类K2个score map
![](https://i.imgur.com/ND4OX6M.png)
![](https://i.imgur.com/Cke20fC.png)

## 人脸检测/行人检测

- 主流数据库
![](https://i.imgur.com/0CsJdpV.png)
- WIDER FACE
- IJB-A
- Caltech


