from PIL import Image
import numpy as np
import cv2
import os
import imageio


class BatchRename():
    '''

    '''

    def __init__(self):

        self.path_now = r'D:\Deep-Learing\NetModel\convnext-U-net\CN_UNET_LOSS1+LOSS2\YY_CN_1\testB'  # 表示正确尺寸的的文件夹


    def resize(self):
        filelist = os.listdir(self.path_now)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        t=1
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path_now), item)
                im = Image.open(src)
                im = np.array(im)

                x = im.shape[0]
                y= im.shape[1]
                for i in range(0, x-1):
                    for j in range(0, y-1):
                        if (im[i,j]> 0 and im[i,j]<28):#24位图时的用法
                            im[i,j] = 0
                        if (im[i,j]> 28 and im[i,j]<56):#24位图时的用法
                            im[i,j] = 28
                        if (im[i,j]>= 56 and im[i,j]<84):#24位图时的用法
                            im[i,j] = 56
                        if (im[i,j]>=84 and im[i,j]<112):#24位图时的用法
                            im[i,j] = 84
                        if (im[i,j]>= 112 and im[i,j]<140):#24位图时的用法
                            im[i,j] = 112
                        if (im[i,j]>= 140 and im[i,j]<168):#24位图时的用法
                            im[i,j] = 140
                        if (im[i,j]>= 168 and im[i,j]<196):#24位图时的用法
                            im[i,j] = 168
                        if (im[i,j]>= 196 and im[i,j]<224):#24位图时的用法
                            im[i,j] = 196
                        if (im[i,j]>= 224 and im[i,j]<252):#24位图时的用法
                            im[i,j] = 224
                im = Image.fromarray(im)
                src = os.path.join(os.path.abspath(self.path_now),"alter")
                if not os.path.exists(src):
                    os.makedirs(src)
                src = os.path.join(os.path.abspath(self.path_now), "alter", item)
                im.save(src)
                print('完成 %d 张' % (t))
                t = t +1


if __name__ == '__main__':
    demo = BatchRename()
    demo.resize()