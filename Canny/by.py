import cv2
import numpy as np
import os
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
def enhanced_edge_detection(image):
    # 使用双边滤波去噪
    filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    # 应用CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrast_enhanced = clahe.apply(filtered)

    # Canny 边缘检测，可能需要根据实际情况调整阈值
    edges = cv2.Canny(contrast_enhanced, 100, 240)
    return edges
def calculate_fitted_curves_for_batch(images,output_folder):
    fitted_images = []  # 存储每张图片拟合曲线后的图像
    cropped_images = []  # 存储截取的图像

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # 创建输出文件夹如果它不存在
    for i in range(images.shape[0]):
        image = images[i]
        edges = enhanced_edge_detection(image)

        y_coords, x_coords = np.where(edges > 0)

        if len(x_coords) == 0 or len(y_coords) == 0:
            print(f"No edges detected in image {i}.")
            fitted_images.append(image)  # 如果没有检测到边缘，则返回原图
            continue

        try:
            # 曲线拟合
            params, _ = curve_fit(lambda x, a, b, c: a * x ** 2 + b * x + c, x_coords, y_coords)
            x_fit = np.linspace(min(x_coords), max(x_coords), num=1000).astype(int)
            y_fit = (params[0] * x_fit ** 2 + params[1] * x_fit + params[2]).astype(int)
            tx = x_fit[0]  # 计算顶点的x坐标
            fitted_image = np.zeros_like(image)
            for x, y in zip(x_fit, y_fit):
                if 0 <= y < fitted_image.shape[0] and 0 <= x < fitted_image.shape[1]:
                    fitted_image[y, x] = 255
            fitted_images.append(fitted_image)
            # 截取图像
            origin_x = int(tx)  # 新原点的x坐标
            origin_y = 512  # 新原点的y坐标

            # 检查是否可以从新原点向右上角截取512x512的图像
            if origin_x + 512 <= image.shape[1] and origin_y - 512 >= 0:
                cropped_image = image[origin_y-512:origin_y, origin_x:origin_x+512]
                cropped_images.append(cropped_image)
                # 保存截取的图像
                cv2.imwrite(os.path.join(output_folder, f'{i}.png'), cropped_image)
            else:
                print(f"Cropping failed for image {i}: out of bounds.")
                cropped_images.append(None)
        except Exception as e:
            print(f"Curve fitting failed for image {i} with error {e}.")
            fitted_images.append(image)
    return fitted_images
def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return np.array(images), filenames

# 加载图像
folder_path = r'C:\data\B_scan'  # 图像存放的文件夹路径
target_path = r'C:\data\B_scan\after'  # 输出存放的文件夹路径
images, filenames = load_images_from_folder(folder_path)

# 调整图像以适应我们的函数，假设我们的函数期望 images 形状为 [batch_size, height, width]
images = images.reshape(-1, images[0].shape[0], images[0].shape[1])

# 调用函数处理图像
fitted_images = calculate_fitted_curves_for_batch(images,target_path)

# 展示原始图像和处理后的图像
# num_images = len(fitted_images)
# fig, axes = plt.subplots(num_images, 2, figsize=(10, num_images * 5))
#
# for i, (orig_img, fit_img) in enumerate(zip(images, fitted_images)):
#     ax1, ax2 = axes[i]
#
#     ax1.imshow(orig_img, cmap='gray')
#     ax1.set_title(f"Original Image {filenames[i]}")
#     ax1.axis('off')
#
#     ax2.imshow(fit_img, cmap='gray')
#     ax2.set_title(f"Fitted Curve Image {filenames[i]}")
#     ax2.axis('off')
#
# plt.tight_layout()
# plt.show()
