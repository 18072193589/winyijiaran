import os
from PIL import Image, ImageChops

savepath = r'D:\Deep-Learing\DP-Data\HW\NEAREST-pre-mask'
savepath2 = r'D:\Deep-Learing\DP-Data\HW\NEAREST-pre-zcr'
targetpath = r'D:\Deep-Learing\DP-Data\HW\正常眼\正视'
width = 1024
height = 1024

class zsj():
    def __init__(self):
        self.temp = 0
        self.temp2 = 0
    def search_files(self,path):
        if os.path.isfile(path):
            if path.endswith('tif'):
                picture_path = path  # 得到图像的绝对路径
                pic_org = Image.open(picture_path)  # 打开图像
                pic_new = pic_org.resize((width, height), Image.NEAREST)  # 图像尺寸修改
                dst = os.path.join(os.path.abspath(savepath), '00' + format(str(self.temp), '0>3s') + '_seg.png')
                pic_new.save(dst)  # 存储文件
                self.temp = self.temp +1
                if(abs(self.temp-self.temp2)>9):
                    print("异常！位置{0},地址{1}".format(self.temp,path))
            if path.endswith('png') :
                if(path.find('View')!=-1 or path.find('iew')!=-1 or path.find('scan')!=-1) and(path.find('N.png')==-1):
                    picture_path = path  # 得到图像的绝对路径
                    pic_org = Image.open(picture_path)  # 打开图像
                    pic_new = pic_org.resize((width, height), Image.NEAREST)  # 图像尺寸修改
                    dst = os.path.join(os.path.abspath(savepath2), '00' + format(str(self.temp2), '0>3s') + '.png')
                    pic_new.save(dst)  # 存储文件
                    self.temp2 = self.temp2 +1
                    if (abs(self.temp - self.temp2) > 9):
                        print("异常！位置{0},地址{1}".format(self.temp,path))
        else:
            for file_name in os.listdir(path):
                sub_path = os.path.join(path, file_name)
                zsj.search_files(self,path=sub_path)

p = zsj()
p.search_files(path=targetpath)