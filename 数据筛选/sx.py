import os
from PIL import Image, ImageChops
#筛选预测出的数据
import os
from PIL import Image, ImageChops
#筛选预测出的数据
savepath = r'D:\Deep-Learing\DP-Data\HW\ZCR\mask'
targetpath = r'D:\Deep-Learing\DP-Data\HW\正常眼'
width = 1024
height = 1024

class zsj():
    def __init__(self):
        self.temp = 0
    def search_files(self,path):
        for file_name in os.listdir(path):
            if file_name.endswith('.tif') :
                picture_path = os.path.join(path, file_name)
                pic_org = Image.open(picture_path)  # 打开图像
                pic_new = pic_org.resize((width, height), Image.NEAREST)  # 图像尺寸修改
                dst = os.path.join(os.path.abspath(savepath), format(str(file_name.split('.')[0])) + '.png')
                pic_new.save(dst)  # 存储文件
                self.temp = self.temp +1
        print(self.temp)

p = zsj()
p.search_files(path=targetpath)