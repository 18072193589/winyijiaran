import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd

class remask():
    def __init__(self):
        self.pre = r'D:\Deep-Learing\DP-Data\yy\00320_20200907003_lyy_OD_2020-09-07_15-13-47_Star R16_81.5888\B-scan_PixelRatio'
        self.mask = r'D:\Deep-Learing\DP-Data\yy\00320_20200907003_lyy_OD_2020-09-07_15-13-47_Star R16_81.5888\predict'
    def msk(self):
        filelist = os.listdir(self.pre)
        filelist2 = os.listdir(self.mask)
        pic_new_path = os.path.join(self.pre, "alter")
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            if item.endswith('.png'):
                img_path = os.path.join(self.pre,item)
                img = cv2.imread(img_path)
                img = np.array(img)
                x = img.shape[0]
                y= img.shape[1]
                for item2 in filelist2:
                    if item2.endswith(item):
                        img2_path = os.path.join(self.mask,item2)
                        img2 = cv2.imread(img2_path)
                        for i in range(2,x-1):
                            for j in range(2,y-1):
                                if (np.array_equal(img2[i,j],[150,150,150]) and np.array_equal(img2[i-1,j],[0,0,0])) or (np.array_equal(img2[i,j],[150,150,150]) and np.array_equal(img2[i,j-1],[0,0,0]))or (np.array_equal(img2[i,j],[150,150,150]) and np.array_equal(img2[i,j+1],[0,0,0])):
                                    img[i, j] = [255, 0, 0]
                                if np.array_equal(img2[i, j],[41,41,41])and np.array_equal(img2[i-1,j],[150,150,150]) or np.array_equal(img2[i, j],[41,41,41])and np.array_equal(img2[i,j-1],[150,150,150])or np.array_equal(img2[i, j],[41,41,41])and np.array_equal(img2[i,j+1],[150,150,150]) :
                                    img[i, j] = [128, 255, 255]
                                if np.array_equal(img2[i, j],[29,29,29])and np.array_equal(img2[i-1,j],[0,0,0]) or np.array_equal(img2[i, j],[29,29,29])and np.array_equal(img2[i-1,j],[41,41,41]) or np.array_equal(img2[i, j],[29,29,29])and np.array_equal(img2[i,j-1],[41,41,41]) or np.array_equal(img2[i, j],[29,29,29])and np.array_equal(img2[i,j+1],[41,41,41]):
                                    img[i, j] = [255, 128, 128]
                                if np.array_equal(img2[i, j],[179,179,179])and np.array_equal(img2[i-1,j],[29,29,29]) or np.array_equal(img2[i, j],[179,179,179])and np.array_equal(img2[i,j-1],[29,29,29]) or np.array_equal(img2[i, j],[179,179,179])and np.array_equal(img2[i,j+1],[29,29,29]):
                                    img[i, j] = [255, 128, 255]
                                if np.array_equal(img2[i, j],[133,133,133])and np.array_equal(img2[i-1,j],[179,179,179]) or np.array_equal(img2[i, j],[133,133,133])and np.array_equal(img2[i,j-1],[179,179,179]) or np.array_equal(img2[i, j],[133,133,133])and np.array_equal(img2[i,j+1],[179,179,179]):
                                    img[i, j] = [255, 255, 0]
                                if np.array_equal(img2[i, j],[62,62,62])and np.array_equal(img2[i-1,j],[133,133,133]) or np.array_equal(img2[i, j],[62,62,62])and np.array_equal(img2[i,j-1],[133,133,133]) or np.array_equal(img2[i, j],[62,62,62])and np.array_equal(img2[i,j+1],[133,133,133]):
                                    img[i, j] = [255, 255, 0]
                                if np.array_equal(img2[i, j],[226,226,226])and np.array_equal(img2[i-1,j],[62,62,62]) or np.array_equal(img2[i, j],[226,226,226])and np.array_equal(img2[i,j-1],[62,62,62]) or np.array_equal(img2[i, j],[226,226,226])and np.array_equal(img2[i,j+1],[62,62,62]):
                                    img[i, j] = [128, 255, 255]
                                if np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i-1,j],[226,226,226]) or np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i,j-1],[226,226,226]) or np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i,j+1],[226,226,226]):
                                    img[i, j] = [255, 0, 128]
                                if np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i+1,j],[0,0,0]) or np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i,j-1],[0,0,0]) or np.array_equal(img2[i, j],[76,76,76])and np.array_equal(img2[i,j+1],[0,0,0]):
                                    img[i, j] = [0, 255, 255]
                                # if np.array_equal(img[i, j],[255,0,255]):
                                #     img[i, j] = [252, 252, 252]
                                # if np.array_equal(img[i, j],[0,0,255]):
                                #     img[i, j] = [0, 0, 0]
                                if (i>0 and i<x-2):
                                    if np.array_equal(img[i,j],[0,0,0]) and (np.array_equal(img[i-1,j],[0,0,0])==False and np.array_equal(img[i+1,j],[0,0,0])==False):
                                        img[i,j] = img[i-1 ,j]
                            print(i)
                                #print(j)
                        crop_img = Image.fromarray(img)
                        dst = os.path.join(pic_new_path,item)
                        crop_img.save(dst)

z = remask()
z.msk()
#[  0 255   0] [100   0 100] [255   0   0]
#[255 255   0] [  0 150 150] [150   0 150]
#[  0 255 255] [  0   0 255]