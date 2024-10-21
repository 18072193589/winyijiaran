from PIL import Image
import os
import random

# 设置训练集测试集输入和输出目录
input_dir_image = r'D:\Deep-Learing\DP-Data\high_js\SW_high_test\mask'
# 仅需改变“文件地址”就可以实现对图片的旋转操作
output_dir_image = input_dir_image

input_dir_segement = r'D:\Deep-Learing\DP-Data\high_js\SW_high_test\pre'
output_dir_segment = input_dir_segement

# 图片数量
input_size_image = len(os.listdir(input_dir_image))
input_size_segment = len(os.listdir(input_dir_segement))

# 随机角度列表生成
Angle = []
for i in range(input_size_image):
    Angle.append(random.randint(1, 359))

i = 0
j = 0
# 对img文件夹的图像进行不同角度的旋转
for filename in os.listdir(input_dir_image):
    if filename.endswith('.png'):
        # 打开图像
        img = Image.open(os.path.join(input_dir_image, filename))
        # 旋转图像并保存
        rotated_img = img.rotate(Angle[i], expand=True)
        rotated_img.save(os.path.join(output_dir_image, f'{Angle[i]}_{filename}'))
        i = i + 1
# 对segment文件夹的图像进行不同角度的旋转
for filename_ in os.listdir(input_dir_segement):
    if filename_.endswith('.png'):
        # 打开图像
        img = Image.open(os.path.join(input_dir_segement, filename_))
        # 旋转图像并保存
        rotated_img = img.rotate(Angle[j], expand=True)
        rotated_img.save(os.path.join(output_dir_segment, f'{Angle[j]}_{filename_}'))
        j = j + 1