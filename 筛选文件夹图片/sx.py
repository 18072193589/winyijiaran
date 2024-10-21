import os
import shutil


def select_and_rename_first_image(source_directory, destination_directory):
    # 如果目标文件夹不存在，则创建它
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # 遍历源文件夹中的每个子文件夹
    for folder_name in os.listdir(source_directory):
        folder_path = os.path.join(source_directory, folder_name)

        if os.path.isdir(folder_path):
            # 获取子文件夹中的所有图片文件
            image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

            if image_files:
                # 选择第一张图片
                first_image = image_files[0]
                source_image_path = os.path.join(folder_path, first_image)

                # 目标图片路径
                destination_image_path = os.path.join(destination_directory, f"{folder_name}.jpg")

                # 复制并重命名图片
                shutil.copy(source_image_path, destination_image_path)
                print(f"已处理文件夹：{folder_name}")


# 源文件夹路径
source_directory = "D:\Deep-Learing\DP-Data\AD\原\left"

# 目标文件夹路径
destination_directory = "D:\Deep-Learing\DP-Data\AD\原"

# 运行函数
select_and_rename_first_image(source_directory, destination_directory)
