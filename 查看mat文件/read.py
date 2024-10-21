import os
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

# 文件夹路径
folder_path = 'D:\Deep-Learing\DP-Data\AMD\Chiu_IOVS_2011\Automatic versus Manual Study'
# 输出文件夹路径
output_folder_path = 'D:\Deep-Learing\DP-Data\AMD\Chiu_IOVS_2011\mask2'
# 获取文件夹中所有的mat文件
mat_files = [f for f in os.listdir(folder_path) if f.endswith('.mat')]
t=0
# 逐个读取和显示mat文件中的图像
for mat_file in mat_files:
    file_path = os.path.join(folder_path, mat_file)
    mat_contents = sio.loadmat(file_path)

    # 假设MAT文件中的数据存储在一个名为'data'的键中
    # 如果键名不同，请根据实际情况修改
    data = mat_contents['images']

    # 检查数据的形状是否为100x64x64
    if data.shape == (512, 1000, 100):
        # 逐个保存100张图像
        for i in range(100):
            averaged_image = data[:,:,i]
            plt.imshow(averaged_image, cmap='gray')
            #plt.title(f'{mat_file} - Image')
            plt.axis('off')  # 隐藏坐标轴

            # 构建图像文件名
            image_name = '00' + format(str(t), '0>3s') + '.png'
            image_path = os.path.join(output_folder_path, image_name)
            t = t+1
            # 保存图像
            plt.savefig(image_path, bbox_inches='tight', pad_inches=0)
            plt.close()
    else:
        print(f'Shape of data in {mat_file} is not (100, 64, 64), it is {data.shape}')
