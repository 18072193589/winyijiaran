import cv2
import os
import numpy as np
from PIL import Image
path=r'D:\Deep-Learing\NetModel\ganseg-master3.0\ganseg-master\hdb_to_canon_v1.2_result\hdb_to_canon_v1\testB'

class hebin():
    def pj(self):
        filelist = os.listdir(path)  # 获取文件路径
        t=0
        pic_new_path = os.path.join(path,"alter")
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            img_name = os.path.join(path, item)
            if item.endswith('pred.png') and item.startswith('testB'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                t=t+1
                if t==1:
                    img1 = cv2.imread(img_name)
                if t==2:
                    img2 = cv2.imread(img_name)
                if t==3:
                    img3 = cv2.imread(img_name)
                    filelist = os.listdir(path)  # 获取文件路径
                    total_num = len(filelist)  # 获取文件长度（个数）
                    # 获取两张图像的宽度和高度
                    h1, w1 = img1.shape[:2]
                    h2, w2 = img2.shape[:2]
                    h3, w3 = img3.shape[:2]

                    # 创建一个新的空白图像，宽度为两张图像的宽度之和，高度为两张图像中高度最大的那张图像的高度
                    new_img = np.zeros((max(h1, h2, h3), w1 + w2 + w3, 3), dtype=np.uint8)

                    # 将第一张图像复制到新图像的左侧
                    new_img[:h1, :w1, :] = img1

                    # 将第二张图像复制到新图像的右侧
                    new_img[:h2, w1:w1 + w2, :] = img2

                    # 将第三张图像复制到新图像的右侧
                    new_img[:h3, w1 + w2:w1 + w2 + w3, :] = img3
                    dst = os.path.join(path, r'alter', item + '.png')
                    im = Image.fromarray(new_img)
                    im.save(dst)
                    # 显示拼接后的图像
                    # cv2.imshow('Image', new_img)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    t=0

zsj = hebin()
zsj.pj()