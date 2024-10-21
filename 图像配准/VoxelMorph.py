import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import cv2
from torchvision import transforms
import voxelmorph as vxm
import matplotlib.pyplot as plt

# 函数：调整图像大小到合适的尺寸
def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

# 读取图像文件夹中的图片
def load_images_from_folder(folder, target_size):
    images = []
    for filename in sorted(os.listdir(folder)):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = resize_image(img, target_size)
            images.append(img)
    return images

# 将图像列表转换为torch张量
def images_to_tensor(images):
    tensor = torch.stack([torch.from_numpy(img).unsqueeze(0).float() for img in images])
    tensor = tensor.unsqueeze(1)  # 添加通道维度
    return tensor

# 目标尺寸 (假设图像应调整到256x256)
target_size = (512, 512)

# 文件夹路径
fixed_image_folder = r'C:\TZBdata\B_scan\after'
moving_image_folder = r'C:\TZBdata\move'

# 读取固定图像和移动图像
fixed_images = load_images_from_folder(fixed_image_folder, target_size)
moving_images = load_images_from_folder(moving_image_folder, target_size)

# 将图像转换为张量
fixed_tensor = images_to_tensor(fixed_images)
moving_tensor = images_to_tensor(moving_images)

# 确保图像张量的形状一致
assert fixed_tensor.shape == moving_tensor.shape, "Fixed and moving image tensors must have the same shape."

# 定义VoxelMorph模型
inshape = fixed_tensor.shape[2:]
unet = vxm.networks.Unet(inshape=inshape)
spatial_transform = vxm.layers.SpatialTransformer(inshape)
model = nn.Sequential(unet, spatial_transform)

# 定义损失函数和优化器
loss_fn = vxm.losses.DiceLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()
    moving_pred, flow = model(moving_tensor, fixed_tensor)
    loss = loss_fn(moving_pred, fixed_tensor)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

# 应用模型进行配准
with torch.no_grad():
    registered_tensor, flow = model(moving_tensor, fixed_tensor)

# 将配准结果保存为图片
output_folder = 'path_to_output_folder'
os.makedirs(output_folder, exist_ok=True)

for i in range(registered_tensor.shape[0]):
    registered_image = registered_tensor[i].squeeze().numpy()
    plt.imsave(os.path.join(output_folder, f'registered_{i:03d}.png'), registered_image, cmap='gray')
