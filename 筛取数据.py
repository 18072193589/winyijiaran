from PIL import Image
import os

file_path = r"D:\Deep-Learing\DP-Data\to zsj\AD\重庆所有患者视网膜分析"    # 原始图像路径
target_path = r"D:\Deep-Learing\DP-Data\to zsj\after"    # 存储图像路径
raw_files = os.walk(file_path)              # 遍历所有图像
width, height = 1024, 640                    # 修改后的图像尺寸大小



for root, dirs, files in raw_files:
    for file in files:                      # 展现各文件
        if file.endswith('.png'):
            picture_path = os.path.join(root, file)    # 得到图像的绝对路径
            pic_org = Image.open(picture_path)               # 打开图像

            pic_new = pic_org.resize((width, height), Image.ANTIALIAS)   # 图像尺寸修改
            _, sub_folder = os.path.split(root)              # 得到子文件夹名字
            pic_new_path = os.path.join(file_path, "alter")
            if not os.path.exists(pic_new_path):
                os.makedirs(pic_new_path)                    # 建立子文件夹
            pic_new_path = os.path.join(pic_new_path, file)  # 新图像存储绝对路径
            pic_new.save(pic_new_path)					     # 存储文件
            print("%s have been resized!" %pic_new_path)
