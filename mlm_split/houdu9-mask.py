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
        self.pre = r'D:\Deep-Learing\DP-Data\MIOU\LY\2'
        # self.mask = r'D:\Deep-Learing\NetModel\util\mlm_split\SW\pre'
        self.list_name = [' ','RNFL', 'GCL+IPL', 'INL', 'OPL', 'HFL+ONL', 'MEZ', 'OS', 'IZ+PRE', 'CHOROID']  # 列名
    def msk(self):
        filelist = os.listdir(self.pre)
        # filelist2 = os.listdir(self.mask)
        pic_new_path = os.path.join(self.pre, "hd")
        ALL = [[], [], [], [], [], [], [], [], []]
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            if item.endswith('296_seg.png'):
                print("当前正在处理{0}".format(item))
                m=[0,0,0,0,0,0,0,0,0]
                s=[0,0,0,0,0,0,0,0,0]
                img_path = os.path.join(self.pre,item)
                img = cv2.imread(img_path)
                img = np.array(img)
                x = img.shape[0]
                y= img.shape[1]
                for i in range(128, 897):
                    m1=0
                    m2=0
                    m3=0
                    m4=0
                    m5=0
                    m6=0
                    m7=0
                    m8=0
                    m9=0
                    m10=0
                    for j in range(2, y - 1):
                        if((np.array_equal(img[j,i],[28,28,28]) and m1==0)):
                            m1 =j
                        if((np.array_equal(img[j,i],[56,56,56]) and m2==0)):
                            m2 =j
                        if((np.array_equal(img[j,i],[84,84,84]) and m3==0)):
                            m3 =j
                        if((np.array_equal(img[j,i],[112,112,112]) and m4==0)):
                            m4 =j
                        if((np.array_equal(img[j,i],[140,140,140]) and m5==0)):
                            m5 =j
                        if((np.array_equal(img[j,i],[168,168,168]) and m6==0)):
                            m6 =j
                        if((np.array_equal(img[j,i],[196,196,196]) and m7==0)):
                            m7 =j
                        if((np.array_equal(img[j,i],[224,224,224]) and m8==0)):
                            m8 =j
                        if((np.array_equal(img[j,i],[252,252,252]) and m9==0)):
                            m9 =j
                        if ((np.array_equal(img[j-1, i], [113, 113, 133]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)
                            or (np.array_equal(img[j-1, i], [114, 114, 114]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)
                            or (np.array_equal(img[j-1, i], [102, 102, 102]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)
                            or (np.array_equal(img[j-2, i], [246, 246, 246]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)
                            or (np.array_equal(img[j-2, i], [255, 255, 255]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)
                            or (np.array_equal(img[j-2, i], [243, 243, 243]) and (np.array_equal(img[j, i], [0, 0, 0])) and m10 == 0)):
                            m10 = j
                    if(m1!=0 and m2!=0):
                        m[0]+=(m2-m1)
                        s[0]+=1
                    if(m2!=0 and m3!=0):
                        m[1]+=(m3-m2)
                        s[1]+=1
                    if(m3!=0 and m4!=0):
                        m[2]+=(m4-m3)
                        s[2]+=1
                    if(m4!=0 and m5!=0):
                        m[3]+=(m5-m4)
                        s[3]+=1
                    if(m5!=0 and m6!=0):
                        m[4]+=(m6-m5)
                        s[4]+=1
                    if(m6!=0 and m7!=0):
                        m[5]+=(m7-m6)
                        s[5]+=1
                    if(m7!=0 and m8!=0):
                        m[6]+=(m8-m7)
                        s[6]+=1
                    if(m8!=0 and m9!=0):
                        m[7]+=(m9-m8)
                        s[7]+=1
                    if(m9!=0 and m10!=0):
                        m[8]+=(m10-m9)
                        s[8]+=1
                if s[0]!=0:
                    ALL[0].append(m[0]/s[0])
                if s[1] != 0:
                    ALL[1].append(m[1] / s[1])
                if s[2] != 0:
                    ALL[2].append(m[2] / s[2])
                if s[3] != 0:
                    ALL[3].append(m[3] / s[3])
                if s[4] != 0:
                    ALL[4].append(m[4] / s[4])
                if s[5] != 0:
                    ALL[5].append(m[5] / s[5])
                if s[6] != 0:
                    ALL[6].append(m[6] / s[6])
                if s[7] != 0:
                    ALL[7].append(m[7] / s[7])
                if s[8] != 0:
                    ALL[8].append(m[8] / s[8])
                #print(ALL[0])

        dataframe = pd.DataFrame(ALL).T
        save = os.path.join(pic_new_path,'9mmhd296'+".csv")
        dataframe.to_csv(save,header=True,index_label=self.list_name)

z = remask()
z.msk()
#[  0 255   0] [100   0 100] [255   0   0]
#[255 255   0] [  0 150 150] [150   0 150]
#[  0 255 255] [  0   0 255]