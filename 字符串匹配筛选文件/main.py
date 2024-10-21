from PIL import Image
import os

file_path = r"D:\Deep-Learing\NetModel\GANSEG5.0\high_SW_result3\high_SW\testB"    # 原始图像路径

raw_files = os.walk(file_path)              # 遍历所有图像
width, height = 1024, 1024                    # 修改后的图像尺寸大小

# 28 56 84 112 140 168 196 224 252

for root, dirs, files in raw_files:
    for file in files:                      # 展现各文件
        if file.endswith('pred.png') and not file.startswith('testA'):
            picture_path = os.path.join(root, file)    # 得到图像的绝对路径
            pic_org = Image.open(picture_path)               # 打开图像

            #pic_new = pic_org.resize((width, height), Image.ANTIALIAS)   # 图像尺寸修改
            _, sub_folder = os.path.split(root)              # 得到子文件夹名字
            pic_new_path = os.path.join(file_path, "alter")
            if not os.path.exists(pic_new_path):
                os.makedirs(pic_new_path)                    # 建立子文件夹
            dst = os.path.join(os.path.abspath(pic_new_path), file.split(".")[0] + '.png')
            pic_new_path = os.path.join(pic_new_path, dst)  # 新图像存储绝对路径
            pic_org.save(pic_new_path)					     # 存储文件
            print("%s have been resized!" %pic_new_path)
