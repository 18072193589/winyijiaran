import queue

import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd


class oil():

    def __init__(self):
        self.name="3D"#存储结果的文件名
        self.path=r'D:\Deep-Learing\NetModel\util\deepblack\img'#目标文件的地址
        self.save_csv=r'D:\Deep-Learing\NetModel\3D\csv'#存储csv的地址
        self.list_name=[' ', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'x4', 'y4', 'z4']#列名
    def XYZ(self):
        filelist = os.listdir(self.path)
        print("==================图像处理中=====================")
        for item in filelist:
            #self.name=item.split(".")[0]
            img_name = os.path.join(self.path, item)
            img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)  # 灰度图像
            img = np.array(img)
            y, x = img.shape
            # 遍历二值图，
            for i in range(3,y-3,2):
                for j in range(3,x - 3,2):
                   if(img[i][j]<55):
                       img[i-1][j-1]=0
                       img[i-1][j]=0
                       img[i-1][j+1]=0
                       img[i][j-1]=0
                       img[i][j]=0
                       img[i][j+1]=0
                       img[i+1][j-1]=0
                       img[i+1][j]=0
                       img[i+1][j+1]=0





            new_img = Image.fromarray(np.uint8(img))
            new_img.save(item)
        return()
    def all(self):
        T.XYZ()
T = oil()

T.all()

