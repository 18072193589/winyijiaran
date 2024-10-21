import cv2
import os
import re
import math
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd
#########################计算各层厚度均值################################
class remask():
    def __init__(self):
        #D:\Deep-Learing\NetModel\GANSEG5.0\high_9_SW_result1\high_9_SW1\testB
        self.pre = r'D:\Deep-Learing\NetModel\connext\YY_HM_result-k1\YY_1\testB'
        self.mask = r'D:\Deep-Learing\DP-Data\HW\HW-5\mask5'
        self.list_name = [' ','RNFL', 'GCL+IPL', 'INL', 'OPL', 'HFL+ONL', 'MEZ', 'OS', 'IZ+PRE', 'CHOROID']  # 列名

    def dice_coefficient(self,pred, target):
        smooth = 1.
        num = pred.size
        m1 =pred.flatten()
        m2 =target.flatten()
        intersection = (m1 * m2).sum()

        return (2. * intersection + smooth) / (m1.sum() + m2.sum() + smooth)

    def msk(self):
        ALL = [[], [], [], [], [], [], [], [], []]
        filelist = os.listdir(self.pre)
        filelist_mask = os.listdir(self.mask)
        # filelist2 = os.listdir(self.mask)
        pic_new_path = os.path.join(self.pre, "hd")
        target_value = [28,56,84,112,140,168,196,224,252]
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            if item.endswith('_pred.png') and item.startswith('testB'):
                temp=0
                print("当前正在处理{0}".format(item))
                img_path = os.path.join(self.pre,item)
                img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
                img = np.array(img)
                nm = re.findall(r'\d+',item)
                for filename in filelist_mask:
                    if nm[0] in filename:
                        img_mask_path = os.path.join(self.mask,filename)
                        img_mask = cv2.imread(img_mask_path,cv2.IMREAD_GRAYSCALE)
                        img_mask = np.array(img_mask)
                        break

                for v in target_value:
                    b_p = np.where(img == v, 1, 0).astype(np.uint8)[:,256:768]
                    b_m = np.where(img_mask == v, 1, 0).astype(np.uint8)[:,256:768]
                    # b_p = np.where(img == v, 1, 0).astype(np.uint8)[:,:]
                    # b_m = np.where(img_mask == v, 1, 0).astype(np.uint8)[:,:]
                    dice_score = self.dice_coefficient(b_p, b_m)
                    print(f"Dice Score: {dice_score.item()}")
                    ALL[temp].append(dice_score)
                    temp = temp + 1
        dataframe = pd.DataFrame(ALL).T
        save = os.path.join(pic_new_path,'0-1024_Dice'+".csv")
        dataframe.to_csv(save,header=True,index_label=self.list_name)
zsj = remask()
zsj.msk()