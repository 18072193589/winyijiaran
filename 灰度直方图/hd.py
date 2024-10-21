import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread(r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9\alter1.0\00001.png')
img2 = cv2.imread(r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9\alter1.8\00001.png')
#图像灰度转换
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#获取图像高度和宽度
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# result = np.zeros((height, width), np.uint8)

#图像灰度上移变换 DB=DA+50
# for i in range(height):
#     for j in range(width):
#         if (int(grayImage[i,j]+50) > 255):
#             gray = 255
#         else:
#             gray = int(grayImage[i,j]+50)
#         result[i,j] = np.uint8(gray)

#计算原图的直方图
hist = cv2.calcHist([img], [0], None, [256], [0,255])

#计算灰度变换的直方图
hist_res = cv2.calcHist([img2], [0], None, [256], [0,255])

#原始图像
plt.figure(figsize=(8, 6))
plt.subplot(221), plt.imshow(img, 'gray'), plt.title("(MiOU:0.45218227662693183)"), plt.axis('off')

#绘制掩膜
plt.subplot(222), plt.plot(hist), plt.title(""), plt.xlabel("x"), plt.ylabel("y")

#绘制掩膜设置后的图像
plt.subplot(223), plt.imshow(img2, 'gray'), plt.title("(MiOU:0.6847575606495161)"), plt.axis('off')

#绘制直方图
plt.subplot(224), plt.plot(hist_res), plt.title(""), plt.xlabel("x"), plt.ylabel("y")
plt.show()