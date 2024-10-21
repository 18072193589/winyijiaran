import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd

class remask():
    def __init__(self):
        self.path = r'D:\Deep-Learing\DP-Data\PD\MCI\mask'

    def msk(self):
        filelist = os.listdir(self.path)
        pic_new_path = os.path.join(self.path, "alter")
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            if item.endswith('.png'):
                img_iame = os.path.join(self.path,item)
                img = cv2.imread(img_iame)
                img = np.array(img)
                x = img.shape[0]
                y= img.shape[1]
                for i in range(x-1):
                    for j in range(y):
                        if np.array_equal(img[i,j],[150,150,150]):
                            img[i, j] = [28, 28, 28]
                        if np.array_equal(img[i, j],[41,41,41]):
                            img[i, j] = [56, 56, 56]
                        if np.array_equal(img[i, j],[29,29,29]):
                            img[i, j] = [84, 84, 84]
                        if np.array_equal(img[i, j],[179,179,179]):
                            img[i, j] = [112, 112, 112]
                        if np.array_equal(img[i, j],[133,133,133]):
                            img[i, j] = [140, 140, 140]
                        if np.array_equal(img[i, j],[62,62,62]):
                            img[i, j] = [168, 168, 168]
                        if np.array_equal(img[i, j],[226,226,226]):
                            img[i, j] = [196, 196, 196]
                        if np.array_equal(img[i, j],[76,76,76]):
                            img[i, j] = [224, 224, 224]
                        # if np.array_equal(img[i, j],[255,0,255]):
                        #     img[i, j] = [252, 252, 252]
                        # if np.array_equal(img[i, j],[0,0,255]):
                        #     img[i, j] = [0, 0, 0]
                        if (i>0 and i<x-2):
                            if np.array_equal(img[i,j],[0,0,0]) and (np.array_equal(img[i-1,j],[0,0,0])==False and np.array_equal(img[i+1,j],[0,0,0])==False):
                                img[i,j] = img[i-1 ,j]
                        print(i)
                        print(j)
                crop_img = Image.fromarray(img)
                dst = os.path.join(pic_new_path,item)
                crop_img.save(dst)

z = remask()
z.msk()
#[  0 255   0] [100   0 100] [255   0   0]
#[255 255   0] [  0 150 150] [150   0 150]
#[  0 255 255] [  0   0 255]