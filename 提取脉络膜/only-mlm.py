import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd
#########################计算各层厚度均值################################
class remask():
    def __init__(self):
        #D:\Deep-Learing\NetModel\GANSEG5.0\high_9_SW_result1\high_9_SW1\testB
        self.pre = r'D:\Deep-Learing\NetModel\GANSEG5.0\LY_9_5_result5\LY_9_5\testB'
        # self.mask = r'D:\Deep-Learing\NetModel\util\mlm_split\SW\pre'
        self.list_name = [' ','RNFL', 'GCL+IPL', 'INL', 'OPL', 'HFL+ONL', 'MEZ', 'OS', 'IZ+PRE', 'CHOROID'] # 列名
        self.list_name2 = [' ', '0-6']  # 列名
    def msk(self,L,R,Name):
        filelist = os.listdir(self.pre)
        # filelist2 = os.listdir(self.mask)
        pic_new_path = os.path.join(self.pre, "after")
        ALL = [[], [], [], [], [], [], [], [], []]
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            #if item.endswith('_pred.png') and item.startswith('testB'):
            if item.endswith('_pred.png') and not item.startswith('testB'):
                print("当前正在处理{0}".format(item))
                img_path = os.path.join(self.pre,item)
                img = cv2.imread(img_path)
                img = np.array(img)
                x = img.shape[0]
                y= img.shape[1]
                for i in range(L, R):
                    for j in range(2, y - 1):
                        if (np.array_equal(img[j,i], [252, 252, 252])):
                            img[j,i] = [0,0,0]
                        else:
                            img[j,i] = [255,255,255]
                crop_img = Image.fromarray(img)
                dst = os.path.join(pic_new_path, item)
                crop_img.save(dst)
                pic_org = Image.open(dst)  # 打开图像
                pic_new = pic_org.resize((1442, 749), Image.ANTIALIAS)  # 图像尺寸修改
                pic_new.save(dst)
z = remask()
z.msk(0, 1024,"0-6mm")
