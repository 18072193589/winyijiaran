import os
from PIL import Image, ImageChops

savepath = r'C:\随便放放数据\TZB\pre'
targetpath = r'C:\随便放放数据\TZB\label刺激后'
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
                #ps = path.split('\\')
                #dst = os.path.join(os.path.abspath(savepath), str(ps[-3]+ps[-2]+ps[-1]))
                dst = os.path.join(os.path.abspath(savepath),'00'+format(str(self.temp),'0>3s') + '.png')
                pic_org.save(dst)  # 存储文件
                self.temp = self.temp +1
        else:
            self.temp = 0
            for file_name in os.listdir(path):
                sub_path = os.path.join(path, file_name)
                zsj.search_files(self,path=sub_path)

p = zsj()
p.search_files(path=targetpath)