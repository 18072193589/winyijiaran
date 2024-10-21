import os
from PIL import Image, ImageChops

savepath = r'D:\Deep-Learing\DP-Data\HW\第三组\原图'
targetpath = r'D:\Deep-Learing\DP-Data\HW\第三组\repeat-2'
width = 1024
height = 1024

class zsj():
    def __init__(self):
        self.temp = 0
    def search_files(self,path):
        if os.path.isfile(path):
            if path.endswith('png'):
                    picture_path = path  # 得到图像的绝对路径
                    pic_org = Image.open(picture_path)  # 打开图像
                    #pic_new = pic_org.resize((width, height), Image.NEAREST)  # 图像尺寸修改
                    dst = os.path.join(os.path.abspath(savepath), '00' + format(str(self.temp), '0>3s') + '.png')
                    pic_org.save(dst)  # 存储文件
                    self.temp = self.temp +1
        else:
            for file_name in os.listdir(path):
                sub_path = os.path.join(path, file_name)
                zsj.search_files(self,path=sub_path)

p = zsj()
p.search_files(path=targetpath)