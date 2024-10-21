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
        self.path = r'D:\Deep-Learing\NetModel\custom_mmseg\data\HW-4\ann_dir\train_rgb'  # 表示需要命名处理的文件夹

        #self.path2 = r'C:\Users\Administrator\Desktop\data_shuoming\fenkuai\img'  # 表示需要命名处理的文件夹
    def rename(self):
        savedpath = self.path
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 0  # 表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)

                im = Image.open(src)
                im = im.convert('L')
                im = im.resize((width, height), Image.NEAREST)  # 图像尺寸修改
                im = np.array(im)
                #im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
                im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
                src = os.path.join(os.path.abspath(self.path),"alter")
                if not os.path.exists(src):
                    os.makedirs(src)
                src = os.path.join(os.path.abspath(self.path), "alter", item)
                img = Image.fromarray(im)
                imageio.imwrite(src,img)
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()