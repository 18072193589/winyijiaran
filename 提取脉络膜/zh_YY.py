from PIL import Image
import numpy as np
import cv2
import os
import imageio


class BatchRename():
    '''
    转化为目标路径下的图像尺寸并且修改像素值
    '''

    def __init__(self):
        self.path_now = r'D:\Deep-Learing\NetModel\connext\YY_HM_result_dice2\YY_2\8位1024'  # 表示需要命名处理的文件夹

        self.path_tar = r'D:\Deep-Learing\DP-Data\一磊老师数据\筛选后的图'  # 表示正确尺寸的的文件夹

        self.size_list_w = []
        self.size_list_h = []
    def resize(self):
        filelist = os.listdir(self.path_tar)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path_tar), item)
                im = Image.open(src)
                self.size_list_w.append(im.size[0])
                self.size_list_h.append(im.size[1])
        filelist = os.listdir(self.path_now)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i=0
        # pic_new_path = os.path.join(self.path_now, "alter")
        # if not os.path.exists(pic_new_path):
        #     os.makedirs(pic_new_path)  # 建立子文件夹
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path_now), item)
                im = Image.open(src)
                im = np.array(im)

                x = im.shape[0]
                y= im.shape[1]
                for i in range(0, x-1):
                    for j in range(2, y - 1):
                        if (im[j,i] == 255):
                            im[j,i] = 0
                        else:
                            im[j,i] = 255
                im = Image.fromarray(im)

                pic_new = im.resize((self.size_list_w[i], self.size_list_h[i]), Image.NEAREST)  # 图像尺寸修改
                pic_new_path = os.path.join(self.path_now, item)  # 新图像存储绝对路径yy2
                pic_new.save(pic_new_path)
                i = i +1
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.resize()