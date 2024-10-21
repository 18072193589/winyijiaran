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
                img2 = cv2.imread(img_iame)
                img2 = np.array(img2)
                x = img2.shape[0]
                y= img2.shape[1]
                for i in range(x-1):
                    for j in range(y):
                        if (np.array_equal(img2[i, j], [150, 150, 150]) and np.array_equal(img2[i - 1, j],
                                                                                           [0, 0, 0])) or (
                                np.array_equal(img2[i, j], [150, 150, 150]) and np.array_equal(img2[i, j - 1],
                                                                                               [0, 0, 0])) or (
                                np.array_equal(img2[i, j], [150, 150, 150]) and np.array_equal(img2[i, j + 1],
                                                                                               [0, 0, 0])):
                            img2[i, j] = [255, 0, 0]
                        if np.array_equal(img2[i, j], [41, 41, 41]) and np.array_equal(img2[i - 1, j], [150, 150,
                                                                                                        150]) or np.array_equal(
                                img2[i, j], [41, 41, 41]) and np.array_equal(img2[i, j - 1],
                                                                             [150, 150, 150]) or np.array_equal(
                                img2[i, j], [41, 41, 41]) and np.array_equal(img2[i, j + 1], [150, 150, 150]):
                            img2[i, j] = [128, 255, 255]
                        if np.array_equal(img2[i, j], [29, 29, 29]) and np.array_equal(img2[i - 1, j],
                                                                                       [0, 0, 0]) or np.array_equal(
                                img2[i, j], [29, 29, 29]) and np.array_equal(img2[i - 1, j],
                                                                             [41, 41, 41]) or np.array_equal(img2[i, j],
                                                                                                             [29, 29,
                                                                                                              29]) and np.array_equal(
                                img2[i, j - 1], [41, 41, 41]) or np.array_equal(img2[i, j],
                                                                                [29, 29, 29]) and np.array_equal(
                                img2[i, j + 1], [41, 41, 41]):
                            img2[i, j] = [255, 128, 128]
                        if np.array_equal(img2[i, j], [179, 179, 179]) and np.array_equal(img2[i - 1, j], [29, 29,
                                                                                                           29]) or np.array_equal(
                                img2[i, j], [179, 179, 179]) and np.array_equal(img2[i, j - 1],
                                                                                [29, 29, 29]) or np.array_equal(
                                img2[i, j], [179, 179, 179]) and np.array_equal(img2[i, j + 1], [29, 29, 29]):
                            img2[i, j] = [255, 128, 255]
                        if np.array_equal(img2[i, j], [133, 133, 133]) and np.array_equal(img2[i - 1, j], [179, 179,
                                                                                                           179]) or np.array_equal(
                                img2[i, j], [133, 133, 133]) and np.array_equal(img2[i, j - 1],
                                                                                [179, 179, 179]) or np.array_equal(
                                img2[i, j], [133, 133, 133]) and np.array_equal(img2[i, j + 1], [179, 179, 179]):
                            img2[i, j] = [255, 255, 0]
                        if np.array_equal(img2[i, j], [62, 62, 62]) and np.array_equal(img2[i - 1, j], [133, 133,
                                                                                                        133]) or np.array_equal(
                                img2[i, j], [62, 62, 62]) and np.array_equal(img2[i, j - 1],
                                                                             [133, 133, 133]) or np.array_equal(
                                img2[i, j], [62, 62, 62]) and np.array_equal(img2[i, j + 1], [133, 133, 133]):
                            img2[i, j] = [255, 255, 0]
                        if np.array_equal(img2[i, j], [226, 226, 226]) and np.array_equal(img2[i - 1, j], [62, 62,
                                                                                                           62]) or np.array_equal(
                                img2[i, j], [226, 226, 226]) and np.array_equal(img2[i, j - 1],
                                                                                [62, 62, 62]) or np.array_equal(
                                img2[i, j], [226, 226, 226]) and np.array_equal(img2[i, j + 1], [62, 62, 62]):
                            img2[i, j] = [128, 255, 255]
                        if np.array_equal(img2[i, j], [76, 76, 76]) and np.array_equal(img2[i - 1, j], [226, 226,
                                                                                                        226]) or np.array_equal(
                                img2[i, j], [76, 76, 76]) and np.array_equal(img2[i, j - 1],
                                                                             [226, 226, 226]) or np.array_equal(
                                img2[i, j], [76, 76, 76]) and np.array_equal(img2[i, j + 1], [226, 226, 226]):
                            img2[i, j] = [255, 0, 128]
                        if (i>0 and i<x-2):
                            if np.array_equal(img2[i,j],[0,0,0]) and (np.array_equal(img2[i-1,j],[0,0,0])==False and np.array_equal(img2[i+1,j],[0,0,0])==False):
                                img2[i,j] = img2[i-1 ,j]
                crop_img = Image.fromarray(img2)
                dst = os.path.join(pic_new_path,item)
                crop_img.save(dst)
z = remask()
z.msk()
#[  0 255   0] [100   0 100] [255   0   0]
#[255 255   0] [  0 150 150] [150   0 150]
#[  0 255 255] [  0   0 255]