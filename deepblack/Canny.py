import cv2 #导入opencv库
 #读取图片
img = cv2.imread(r"D:\Deep-Learing\NetModel\util\deepblack\img\00009.png")
#进行canny边缘检测
edge = cv2.Canny(img,50,150)
#保存结果
cv2.imwrite('test.jpg',edge)
