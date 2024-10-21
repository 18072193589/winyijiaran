from PIL import Image
import numpy as np
import cv2
import os
import imageio

width, height = 1024, 1024  # 修改后的图像尺寸大小
class BatchRename():
    '''
    批量重命名文件夹中的图片文件（其他文件也可）
    '''
    #Image.NEAREST 不增加额外灰度，用原灰度填充
    def __init__(self):
        self.path = r'D:\Deep-Learing\NetModel\convnext-U-net\HM_UNET_CE_loss1+loss2\YY_1\testB'  # 表示需要命名处理的文件夹

        #self.path2 = r'C:\Users\Administrator\Desktop\data_shuoming\fenkuai\img'  # 表示需要命名处理的文件夹
    def rename(self):
        new_classes = np.array([0, 28, 56, 84, 112, 140, 168, 196, 224, 252])
        old_classes = np.array([0, 28, 57, 85, 113, 142, 170, 198, 227, 255])
        savedpath = self.path
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 0  # 表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)

                im = Image.open(src)
                im = np.array(im)
                # # 将不在数组范围内的像素值置为0
                # im[~np.isin(im, old_classes)] = 0
                mapped_array = np.zeros_like(im)
                for old_class, new_class in zip(old_classes, new_classes):
                    mapped_array[im == old_class] = new_class
                src = os.path.join(os.path.abspath(self.path),"alter")
                if not os.path.exists(src):
                    os.makedirs(src)
                src = os.path.join(os.path.abspath(self.path), "alter", item)
                img = Image.fromarray(mapped_array)
                imageio.imwrite(src,img)
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()