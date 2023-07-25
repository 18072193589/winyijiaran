import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd

class remask():
    def __init__(self):
        self.path = r'D:\Deep-Learing\DP-Data\Split-OCT\1024-3type-8\RTvue\pre'

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
                        if np.array_equal(img[i,j],[0,255,0]):
                            img[i, j] = [30, 30, 30]
                        if np.array_equal(img[i, j],[100,0,100]):
                            img[i, j] = [60, 60, 60]
                        if np.array_equal(img[i, j],[255,0,0]):
                            img[i, j] = [90, 90, 90]
                        if np.array_equal(img[i, j],[255,255,0]):
                            img[i, j] = [120, 120, 120]
                        if np.array_equal(img[i, j],[0,150,150]):
                            img[i, j] = [150, 150, 150]
                        if np.array_equal(img[i, j],[150,0,150]):
                            img[i, j] = [180, 180, 180]
                        if np.array_equal(img[i, j],[0,255,255]):
                            img[i, j] = [210, 210, 210]
                        if np.array_equal(img[i, j],[0,0,255]):
                            img[i, j] = [240, 240, 240]
                        if np.array_equal(img[i, j],[0,0,255]):
                            img[i, j] = [0, 0, 0]
                        if (i>0 and i<x-2):
                            if np.array_equal(img[i,j],[0,0,0]) and (np.array_equal(img[i-1,j],[0,0,0])==False and np.array_equal(img[i+1,j],[0,0,0])==False):
                                img[i,j] = img[i-1 ,j]
                crop_img = Image.fromarray(img)
                dst = os.path.join(pic_new_path,item)
                crop_img.save(dst)
z = remask()
z.msk()
#[  0 255   0] [100   0 100] [255   0   0]
#[255 255   0] [  0 150 150] [150   0 150]
#[  0 255 255] [  0   0 255]