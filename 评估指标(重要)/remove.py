from PIL import Image
import os

file_path = r"D:\Deep-Learing\NetModel\GANSEG5.0\YY_HM_result4-2\YY_4\testB"    # 原始图像路径

raw_files = os.walk(file_path)              # 遍历所有图像
width, height = 1024, 1024                    # 修改后的图像尺寸大小

# 28 56 84 112 140 168 196 224 252

for root, dirs, files in raw_files:
    for file in files:                      # 展现各文件
        if file.startswith('testA') or file.startswith('trainB')or not file.endswith('pred.png'):
            picture_path = os.path.join(root, file)  # 得到图像的绝对路径
            os.remove(picture_path)
            print("%s have been remove!" %file)
