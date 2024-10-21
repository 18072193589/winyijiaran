import cv2
import numpy as np

# 读取分割后的图像
segmentation_image = cv2.imread(r'D:\Deep-Learing\NetModel\convnext-U-net\Ture_data\CN\00008_seg.png', cv2.IMREAD_GRAYSCALE)

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

# 转换为彩色图像
colored_image = cv2.cvtColor(segmentation_image, cv2.COLOR_GRAY2BGR)

# 遍历每个灰度值
for value, color in colors.items():
    # 找到边界
    edges = cv2.Canny((segmentation_image == value).astype(np.uint8) * 255, 100, 200)

    # 在边界上画线
    colored_image[edges > 0] = color

# 保存或显示结果图像
cv2.imwrite('CN.png', colored_image)
#cv2.imshow('Segmentation with Boundaries', colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

