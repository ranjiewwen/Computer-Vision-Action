# 第十讲_图像检索 Image Retrieval

- 刚要
![](https://i.imgur.com/7cHhdMi.png)
- 主要是图像预处理和特征提取+相似度计算
- 
### 相似颜色检索

- 算法结构
![](https://i.imgur.com/xirnXCc.png)

- 颜色特征提取：统计图片的颜色成分
![](https://i.imgur.com/gBzRkMW.png)
- 颜色特征相似度计算
![](https://i.imgur.com/eXjpPrf.png)

- 色差距离
- 发展：欧式距离->CIEDE1994->CIEDE2000
![](https://i.imgur.com/n2ku9KP.png)

- EMD距离
![](https://i.imgur.com/vRGdrXP.png)

### 相似纹理检索

- 纹理
![](https://i.imgur.com/MdzUoT6.png)
- 算法结构
![](https://i.imgur.com/BOHkiGv.png)
- Gabor滤波器组
![](https://i.imgur.com/ag3VGzC.png)

### 相似形状检索

- PHOG形状特征提取
![](https://i.imgur.com/SYehhNo.png)
- 相似度计算
![](https://i.imgur.com/F0BcLrh.png)


### 相似局部特征检索

- 局部特征点特征提取
![](https://i.imgur.com/ID31UTm.png)

### 词包 bag of visual world

- 视觉词汇的字典
![](https://i.imgur.com/fwenIiK.png)
![](https://i.imgur.com/pAPcjiL.png)

## 大数据下的索引加速

### KD-tree

- 理解
![](https://i.imgur.com/mlapDcW.png)
![](https://i.imgur.com/6pd0WPu.png)

### 局部敏感哈希

- 概念
![](https://i.imgur.com/De2crCW.png)
![](https://i.imgur.com/ymuG2TJ.png)
![](https://i.imgur.com/N9fYMLb.png)
![](https://i.imgur.com/kzrfHNv.png)

- P-stable LSH
![](https://i.imgur.com/zNLABmN.png)

- 如何集成LSH
- 单表和多表结构
![](https://i.imgur.com/jWD8jHW.png)

### 代码讲解

- CBIR_TF
- 基于内容的图片检索CBIR（Content Based Image Retrieval）
- LIRE(Lucene Image Retrieval)相似图像索引和搜索机制