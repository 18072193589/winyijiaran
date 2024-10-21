import os

import cv2
import numpy as np

# 读取图像
image_path = r'D:\Deep-Learing\NetModel\util\9cut\image\00000.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 具体的灰度值
gray_values = [0, 28, 56, 84, 112, 140, 168, 196, 224, 252]

# 创建一个字典来存储分割后的图像
separated_images = {}

for value in gray_values:
    # 创建一个掩模，其中灰度值等于当前值的像素被设置为原值，其他为0
    mask = np.where(image == value, 255, 0).astype(np.uint8)

    # 使用掩模来生成图像
    separated_images[value] = mask

    pre_dir = os.path.dirname(image_path)
    # 保存或处理每个分割后的图像
    cv2.imwrite(os.path.join((pre_dir),f'image_{value}.jpg'), mask)

# 现在你有了基于特定灰度值的10张分割图像
