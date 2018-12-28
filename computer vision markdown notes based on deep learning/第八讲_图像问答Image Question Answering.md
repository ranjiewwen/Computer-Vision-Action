
# 第八讲_图像问答Image Question  Answering

- 课程结构
![](https://i.imgur.com/Gk4r6EN.png)
- 图像问答的描述
![](https://i.imgur.com/s9cina3.png)
- 具备一系列AI能力：细分识别，物体检测，动作识别，常识推理，知识库推理.....
- 先要根据问题，判断什么任务
- 图像问题与图像描述的关系
![](https://i.imgur.com/nUbvF9a.png)
- 研究的难点和挑战
![](https://i.imgur.com/7g45tBt.png)
- 研究方向
![](https://i.imgur.com/CoRElTo.png)

### 数据集

- COCO-QA来源MSCOCO
- VQA（visual question answering）
- 平衡数据集V1.9-->V2.0
- Visual7W---Visual Genome的子集

### 图像问答模型

- 模型
![](https://i.imgur.com/HeQa9m2.png)
- 基本都是VGG-Net和ResNet,LSTM模型
- LSTM：三个门和记忆状态
![](https://i.imgur.com/jGaiPMX.png)
- 基本模型
![](https://i.imgur.com/avcqVZ4.png)
![](https://i.imgur.com/o01ISLd.png)

### 模型增强：注意机制

- 基本模型
![](https://i.imgur.com/Ba953EM.png)
![](https://i.imgur.com/kQpuEeH.png)

### 模型增强：外部知识库

- 基本模型
![](https://i.imgur.com/0o6oEWd.png)
- 属性预测模型