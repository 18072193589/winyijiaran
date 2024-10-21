import os
from PIL import Image, ImageChops

savepath = r'D:\Deep-Learing\DP-Data\高度近视\批量生成-正常人\pre2'
targetpath = r'D:\Deep-Learing\DP-Data\高度近视\正常眼'
targetpath2 = r'D:\Deep-Learing\DP-Data\高度近视\正常眼\raw'
width = 1024
height = 1024

class zsj():
    def __init__(self):
        self.temp = 0
    def search_files(self,path,path2):
        for file_name in os.listdir(path):
            if file_name.endswith('tif'):
                for file_name2 in os.listdir(path2):
                    if file_name2.split('.')[0]==file_name.split('.')[0]:
                        picture_path = os.path.join(path2, file_name2)
                        pic_org = Image.open(picture_path)  # 打开图像
                        pic_new = pic_org.resize((width, height), Image.ANTIALIAS)  # 图像尺寸修改
                        dst = os.path.join(os.path.abspath(savepath), format(str(file_name2.split('.')[0])) + '.png')
                        pic_new.save(dst)  # 存储文件
p = zsj()
p.search_files(path=targetpath,path2=targetpath2)