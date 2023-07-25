import numpy as np
import cv2 as cv
#该函数返回的第一个值就是输入的thresh值，第二个就是处理后的图像
img = cv.imread(r'D:\Deep-Learing\NetModel\util\deepblack\img\testB_00033_pred.png',0)
retVal, a_img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
print("使用opencv函数的方法：" + str(retVal))	# 结果为 134
cv.imshow("a_img",a_img)
cv.waitKey()
