import numpy as np
import cv2
import os

# 假设 segmentation_result 是你的分割结果图像（二维numpy数组）
# 灰度层次值列表
grayscale_values = [0, 28, 56, 84, 112, 140, 168, 196, 224, 252]

# 定义每个层次对应的颜色（BGR格式）
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
          (255, 0, 255), (0, 255, 255), (128, 0, 128), (128, 128, 0),
          (0, 128, 128), (255, 0, 0)]

# 创建保存图片的文件夹
output_dir = r'D:\Deep-Learing\NetModel\util\9cut\mask'
os.makedirs(output_dir, exist_ok=True)
segmentation_result = cv2.imread(r'D:\Deep-Learing\NetModel\util\9cut\mask\00000_seg.png', cv2.IMREAD_GRAYSCALE)
# 遍历每一个灰度值，生成对应的图层、检测边界并突出显示
for i, value in enumerate(grayscale_values):
    # 创建一个二值化的图像，灰度值为 value 的位置设置为 255，其余位置为 0
    layer_image = np.where(segmentation_result == value, 255, 0).astype(np.uint8)

    # 查找轮廓
    contours, _ = cv2.findContours(layer_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建一个彩色图像，用于绘制边界
    color_layer_image = cv2.cvtColor(layer_image, cv2.COLOR_GRAY2BGR)

    # 绘制轮廓，用对应的颜色突出显示
    cv2.drawContours(color_layer_image, contours, -1, colors[i], 2)

    # 保存图片
    output_path = os.path.join(output_dir, f'layer_{value}_with_boundary.png')
    cv2.imwrite(output_path, color_layer_image)

    print(f"Layer with grayscale value {value} saved with boundaries as {output_path}")
