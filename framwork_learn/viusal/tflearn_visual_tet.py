# -*- coding: utf-8 -*-

""" Convolutional Neural Network for MNIST dataset classification task.
References:
    Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based
    learning applied to document recognition." Proceedings of the IEEE,
    86(11):2278-2324, November 1998.
Links:
    [MNIST Dataset] http://yann.lecun.com/exdb/mnist/
"""

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

# Data loading and preprocessing
import tflearn.datasets.mnist as mnist
X, Y, testX, testY = mnist.load_data(one_hot=True)
X = X.reshape([-1, 28, 28, 1])
testX = testX.reshape([-1, 28, 28, 1])

# Building convolutional network
network = input_data(shape=[None, 28, 28, 1], name='input')
h_conv1 = conv_2d(network, 32, 3, activation='relu', regularizer="L2",name="conv1")
network = max_pool_2d(h_conv1, 2,name="pool1")
network = local_response_normalization(network)
network = conv_2d(network, 64, 3, activation='relu', regularizer="L2",name="conv2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = fully_connected(network, 128, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 256, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 10, activation='softmax')
network = regression(network, optimizer='adam', learning_rate=0.01,
                     loss='categorical_crossentropy', name='target')

# Training
model = tflearn.DNN(network, tensorboard_verbose=3)

import os
filename = r'/my_model.tflearn'
if os.path.exists(filename):
    model.fit({'input': X}, {'target': Y}, n_epoch=1,
              validation_set=({'input': testX}, {'target': testY}),
              snapshot_step=100, show_metric=True, run_id='convnet_mnist')
    # Save a model
    print("save model....")
    model.save('my_model.tflearn')
else:
    # Load a model
    model.load("my_model.tflearn")
    # model.get_weights(network.W)


# ------------------
# Retrieving weights
# ------------------

# Retrieve a layer weights, by layer name:
dense1_vars = tflearn.variables.get_layer_variables_by_name('conv1')
# Get a variable's value, using model `get_weights` method:
print("Dense1 layer weights:")
print(model.get_weights(dense1_vars[0]).shape)
# Or using generic tflearn function:
print("Dense1 layer biases:")
with model.session.as_default():
    print(tflearn.variables.get_value(dense1_vars[1]).shape)


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# imput image
fig2, ax2 = plt.subplots(figsize=(2, 2))
ax2.imshow(np.reshape(X[0], (28, 28)))
#plt.show()
print("X[0] is :",Y[0])

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST/mnist', one_hot=True)
# 第一层的卷积输出的特征图
# x 是手写图像的像素值,y 是图像对应的标签
x = tf.placeholder(tf.float32, [1,28,28,1])
y = tf.placeholder(tf.float32, [1,10])
# 全局变量进行初始化的Operation
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    input_image = tf.reshape(X[0], [-1, 28, 28, 1]) #X[0].reshape(1,28,28,1)# tf.reshape(X[0], [-1, 28, 28, 1]) #X[0].reshape(1,28,28,1)##

    #input_image = mnist.train.images[11:12]
    #input_image=input_image.reshape(1,28,28,1)

    # X[0]=np.array(X[0])
    # X[0]=X[0].astype(float)
    # input_image=np.reshape(X[0],[1,28,28,1])
    print(input_image.shape,input_image.dtype)

    #x_r= sess.run(input_image)
    #x_r=tf.convert_to_tensor(input_image)
    #print(x_r.dtype)
    conv1_16 = sess.run(h_conv1, feed_dict={x: input_image})  # [16, 28, 28 ,1]
    conv1_reshape = sess.run(tf.reshape(conv1_16, [32, 1, 28, 28]))
    fig3, ax3 = plt.subplots(nrows=1, ncols=32, figsize=(16, 1))
    for i in range(32):
        ax3[i].imshow(conv1_reshape[i][0])  # tensor的切片[batch, channels, row, column]

    plt.title('Conv1 16x28x28')
    plt.show()

# It is also possible to retrieve a layer weights through its attributes `W`
# and `b` (if available).
# Get variable's value, using model `get_weights` method:
dense2_vars = tflearn.variables.get_layer_variables_by_name('conv2')
print("Dense2 layer weights:")
print(model.get_weights(dense2_vars[0]).shape)
# Or using generic tflearn function:
print("Dense2 layer biases:")
with model.session.as_default():
    print(tflearn.variables.get_value(dense1_vars[1]).shape)


