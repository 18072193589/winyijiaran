import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取参考图像和待配准图像
reference_image = cv2.imread('00000p.png', cv2.IMREAD_GRAYSCALE)
moving_image = cv2.imread('00001p.png', cv2.IMREAD_GRAYSCALE)

# 使用ORB特征检测器
orb = cv2.ORB_create()

# 找到图像的关键点和描述符
keypoints1, descriptors1 = orb.detectAndCompute(reference_image, None)
keypoints2, descriptors2 = orb.detectAndCompute(moving_image, None)

# 创建BFMatcher对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 匹配描述符
matches = bf.match(descriptors1, descriptors2)

# 按照距离排序
matches = sorted(matches, key=lambda x: x.distance)

# 提取匹配的关键点位置
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

# 计算仿射变换矩阵
matrix, mask = cv2.estimateAffinePartial2D(points2, points1)

# 应用变换矩阵到待配准图像
height, width = reference_image.shape
aligned_image = cv2.warpAffine(moving_image, matrix, (width, height))

# 显示结果
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Reference Image')
plt.imshow(reference_image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Moving Image')
plt.imshow(moving_image, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Aligned Image')
plt.imshow(aligned_image, cmap='gray')

plt.show()
