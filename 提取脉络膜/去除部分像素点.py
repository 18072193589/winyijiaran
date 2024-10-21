from PIL import Image
import numpy as np
import cv2
import os
import imageio


class BatchRename():
    '''

    '''

    def __init__(self):

        self.path_now = r'D:\Deep-Learing\DP-Data\一磊老师数据\筛选后的图'  # 表示正确尺寸的的文件夹


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
                for i in range(400, x-1):
                    for j in range(2, 200):
                        if (np.array_equal(im[i,j], [255, 255, 255])):#24位图时的用法
                            im[i,j] = [50,50,50]
                im = Image.fromarray(im)

                pic_new_path = os.path.join(self.path_now, item)  # 新图像存储绝对路径yy2
                im.save(pic_new_path)
                print('完成 %d 张' % (t))
                t = t +1


if __name__ == '__main__':
    demo = BatchRename()
    demo.resize()