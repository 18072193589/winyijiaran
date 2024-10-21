from PIL import Image
import os

file_path = r"D:\Deep-Learing\DP-Data\rtvue\image"    # 原始图像路径

raw_files = os.walk(file_path)              # 遍历所有图像
width, height = 512, 512                    # 修改后的图像尺寸大小

# 28 56 84 112 140 168 196 224 252

for root, dirs, files in raw_files:
    for file in files:                      # 展现各文件
        if file.startswith('testA') or  file.endswith('seg.png'):
            picture_path = os.path.join(root, file)  # 得到图像的绝对路径
            os.remove(picture_path)
            print("%s have been remove!" %file)
