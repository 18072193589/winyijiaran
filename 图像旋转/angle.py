import os
import cv2
from PIL import Image
class BatchRename():
    '''
    批量重命名文件夹中的图片文件（其他文件也可）
    '''

    def __init__(self):
        self.path = r'D:\Deep-Learing\DP-Data\yy\OD01'  # 表示需要命名处理的文件夹

        #self.path2 = r'C:\Users\Administrator\Desktop\data_shuoming\fenkuai\img'  # 表示需要命名处理的文件夹
    def reangle(self):
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 1  # 表示文件的命名是从1开始的
        pic_new_path = os.path.join(self.path, "angle")
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
        for item in filelist:
            if item.endswith('.tif'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                img = cv2.imread(src)
                #将图像位深度改为8即灰度图
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                size=img.shape
                r = size[1]
                c = size[0]
                img = img[r-1: :-1,:]
                image = Image.fromarray(img)
                image.save(os.path.join(pic_new_path,item))
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.reangle()