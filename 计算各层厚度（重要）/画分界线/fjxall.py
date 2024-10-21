import cv2
import numpy as np
import os

# 设置图像文件夹路径（包含中文路径）
folder_path = r'D:\Deep-Learing\NetModel\util\计算各层厚度（重要）\画分界线\HMt'

# 定义每个灰度值的颜色
colors = {
    0: (0, 0, 255),  # 红色
    28: (0, 255, 0),  # 绿色
    56: (255, 0, 0),  # 蓝色
    84: (0, 255, 255),  # 黄色
    112: (255, 255, 0),  # 青色
    140: (255, 0, 255),  # 紫色
    168: (0, 0, 255),  # 灰色
    196: (0, 128, 128),  # 深青色
    224: (128, 0, 128),  # 深紫色
    252: (55, 5, 155)  # 橙色
}


# 用于读取中文路径的图像
def imread_unicode(image_path):
    stream = open(image_path, "rb")
    bytes_array = bytearray(stream.read())
    numpy_array = np.asarray(bytes_array, dtype=np.uint8)
    return cv2.imdecode(numpy_array, cv2.IMREAD_GRAYSCALE)


# 遍历文件夹下所有的图像
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        file_path = os.path.join(folder_path, filename)

        # 读取分割后的图像（支持中文路径）
        segmentation_image = imread_unicode(file_path)

        # 检查图像是否读取成功
        if segmentation_image is None:
            print(f"图像读取失败: {file_path}")
            continue  # 跳过此图像并处理下一个

        # 转换为彩色图像
        colored_image = cv2.cvtColor(segmentation_image, cv2.COLOR_GRAY2BGR)

        # 遍历每个灰度值，绘制边界
        for value, color in colors.items():
            # 找到边界
            edges = cv2.Canny((segmentation_image == value).astype(np.uint8) * 255, 100, 200)

            # 在边界上画线
            colored_image[edges > 0] = color

        # 保存并覆盖原图像（支持中文路径保存）
        cv2.imencode('.png', colored_image)[1].tofile(file_path)

print("所有图像处理完成并已覆盖原图像。")
