import cv2
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import pandas as pd

class remask():
    def __init__(self):
        self.pre = r'D:\Deep-Learing\NetModel\util\mlm_split\SW\pre'
        self.list_name = ['y','ILM', 'NFL_GCL', 'IPL_INL', 'INL_OPL', 'OPL_ONL', 'ELM', 'IS_OS', 'PRE', 'CHOROID','under_CHO']  # 列名
    def msk(self):
        filelist = os.listdir(self.pre)
        pic_new_path = os.path.join(self.pre, "data_save")

        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            ALL = [[], [], [], [], [], [], [], [], [], []]
            if item.endswith('.png'):
                m=[0,0,0,0,0,0,0,0,0]
                s=[0,0,0,0,0,0,0,0,0]
                img_path = os.path.join(self.pre,item)
                img = cv2.imread(img_path)
                img = np.array(img)
                x = img.shape[0]
                y= img.shape[1]
                for i in range(2, x):
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
                    for j in range(2, y - 3):
                        if((np.array_equal(img[j,i],[28,28,28]) and m1==0)):
                            m1 =j
                            ALL[0].append(j)
                        if((np.array_equal(img[j,i],[56,56,56]) and m2==0)):
                            m2 =j
                            ALL[1].append(j)
                        if((np.array_equal(img[j,i],[84,84,84]) and m3==0)):
                            m3 =j
                            ALL[2].append(j)
                        if((np.array_equal(img[j,i],[112,112,112]) and m4==0)):
                            m4 =j
                            ALL[3].append(j)
                        if((np.array_equal(img[j,i],[140,140,140]) and m5==0)):
                            m5 =j
                            ALL[4].append(j)
                        if((np.array_equal(img[j,i],[168,168,168]) and m6==0)):
                            m6 =j
                            ALL[5].append(j)
                        if((np.array_equal(img[j,i],[196,196,196]) and m7==0)):
                            m7 =j
                            ALL[6].append(j)
                        if((np.array_equal(img[j,i],[224,224,224]) and m8==0)):
                            m8 =j
                            ALL[7].append(j)
                        if((np.array_equal(img[j,i],[252,252,252]) and m9==0)):
                            m9 =j
                            ALL[8].append(j)
                        if(np.array_equal(img[j-1,i],[252,252,252]) and (np.array_equal(img[j, i], [0, 0, 0] or np.array_equal(img[j+1, i], [0, 0, 0] or np.array_equal(img[j+2, i], [0, 0, 0])))) and m10==0):
                        # if ((np.array_equal(img[j-1, i], [252, 252, 252])  and m10 == 0 or (np.array_equal(img[j, i], [0, 0, 0])) or (np.array_equal(img[j+1, i], [0, 0, 0])) or (np.array_equal(img[j+2, i], [0, 0, 0])) or (np.array_equal(img[j+3, i], [0, 0, 0])))):
                            m10 = j
                            ALL[9].append(j)
                    if(m1==0):
                        ALL[0].append('')
                    if(m2==0):
                        m2=m1
                        ALL[1].append(m1)
                    if(m3==0):
                        m3=m2
                        ALL[2].append(m2)
                    if(m4==0):
                        m4=m3
                        ALL[3].append(m3)
                    if(m5==0):
                        m5=m4
                        ALL[4].append(m4)
                    if(m6==0):
                        m6=m5
                        ALL[5].append(m5)
                    if(m7==0):
                        m7=m6
                        ALL[6].append(m6)
                    if(m8==0):
                        m8=m7
                        ALL[7].append(m7)
                    if(m9==0):
                        m9=m8
                        ALL[8].append(m8)
                    if(m10==0):
                        ALL[9].append(m9)
            dataframe = pd.DataFrame(ALL).T
            save = os.path.join(pic_new_path, item.split('.')[0] + ".csv")
            dataframe.to_csv(save, header=True, index_label=self.list_name)



z = remask()
z.msk()
