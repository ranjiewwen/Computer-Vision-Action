## Tensorflow

- 数据加载方式：[finetune_alexnet_with_tensorflow](https://github.com/kratzert/finetune_alexnet_with_tensorflow)
- [Example of TensorFlows new Input Pipeline](https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html)

```python

import matplotlib.pyplot as plt
import tensorflow as tf
import utility
import os

IMAGE_DIR_PATH = 'data/training/images'
MASK_DIR_PATH = 'data/training/masks'
BATCH_SIZE = 4

plt.ioff()

# create list of PATHS
image_paths = [os.path.join(IMAGE_DIR_PATH, x) for x in os.listdir(IMAGE_DIR_PATH) if x.endswith('.png')]
mask_paths = [os.path.join(MASK_DIR_PATH, x) for x in os.listdir(MASK_DIR_PATH) if x.endswith('.png')]

# Where image_paths[0] = '/data/training/images/image_0.png' 
# And mask_paths[0] = 'data/training/masks/image_0_mask.png'

# Parse the images and masks, and return the data in batches, augmented optionally
data, init_op = utility.data_batch(image_paths, mask_paths, augment=True, batch_size=BATCH_SIZE)
# Get the image and mask op from the returned dataset
aug_image_tensor, aug_mask_tensor = data


with tf.Session() as sess:
  sess.run(init_op)
  # Evaluate the tensors
  aug_image, aug_mask = sess.run([aug_image_tensor, aug_mask_tensor])
                                 
  # Confirming everything is working by visualizing
  plt.figure('augmented image')
  plt.imshow(aug_image[0, :, :, :])
  plt.figure('augmented mask')
  plt.imshow(aug_mask[0, :, :])
  plt.show()
  # Do whatever you want now, like creating a feed dict and train your models
```

## Pytorch


## Keras
