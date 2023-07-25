import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

src = cv.imread(r"D:\Deep-Learing\NetModel\util\deepblack\img\00008.png", 0)  # 直接以灰度图方式读入
img = src.copy()

# 计算Sobel卷积结果
# x = cv.Sobel(img, cv.CV_16S, 1, 0)
# y = cv.Sobel(img, cv.CV_16S, 0, 1)
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)
# 转换数据 并 合成
Scale_absX = cv.convertScaleAbs(x)  # 格式转换函数
Scale_absY = cv.convertScaleAbs(y)
result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)  # 图像混合

# 显示图像
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("原图")
axes[1].imshow(result, cmap=plt.cm.gray)
axes[1].set_title("Sobel检测后结果")
plt.show()