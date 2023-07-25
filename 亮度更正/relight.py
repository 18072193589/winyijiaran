from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import os
image = img_as_float(data.moon())
class BatchRename():
    '''
    批量重命名文件夹中的图片文件（其他文件也可）
    '''

    def __init__(self):
        self.path = r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9\testB'  # 表示需要命名处理的文件夹
        self.dir = r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9'  #上级目录
        #self.path2 = r'C:\Users\Administrator\Desktop\data_shuoming\fenkuai\img'  # 表示需要命名处理的文件夹
    def rename(self):
        savedpath = self.path
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 1  # 表示文件的命名是从1开始的
        for t in range(3,20):
            for item in filelist:
                if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                    # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                    src = os.path.join(os.path.abspath(self.path), item)
                    img = cv2.imread(src)
                    img = exposure.adjust_gamma(img,t/10)
                    src = os.path.join(os.path.abspath(self.dir),"alter{0}".format(t/10))
                    if not os.path.exists(src):
                        os.makedirs(src)
                    src = os.path.join(os.path.abspath(self.dir), "alter{0}".format(t/10), item)
                    cv2.imwrite(src, img)  # 填转换后的图片存储地址，若在同一目录，则注意不要重名
            print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()