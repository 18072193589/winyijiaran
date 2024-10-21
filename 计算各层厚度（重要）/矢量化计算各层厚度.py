import numpy as np
import os
import pandas as pd
import cv2

class remask():
    def __init__(self):
        self.pre = r'D:\Deep-Learing\NetModel\convnext-U-net\HM_UNET_LOSS1+LOSS2\YY_1\testB'
        self.list_name = [' ', 'RNFL', 'GCL+IPL', 'INL', 'OPL', 'HFL+ONL', 'MEZ', 'OS', 'IZ+PRE', 'CHOROID']
        self.original_height = 1201  # 原始高度
        self.original_width = 751  # 原始宽度
        self.new_size = 1024  # 新尺寸
        self.pixel_to_mm_ratio = 4 / 1021  # 每个像素对应的mm长度
        self.pixel_to_um_ratio = self.pixel_to_mm_ratio * 1000  # 转换为um
        self.vertical_scale = self.new_size / self.original_height  # 纵向拉伸比例

    def msk(self):
        filelist = os.listdir(self.pre)
        pic_new_path = os.path.join(self.pre, "HD")
        ALL = [[] for _ in range(10)]

        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)

        for item in filelist:
            if item.endswith('.png') or item.startswith('testB'):
                print("当前正在处理{0}".format(item))

                img_path = os.path.join(self.pre, item)
                img = cv2.imread(img_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = np.array(img)

                # 只处理[256, 768]的范围
                img_section = img[256:768, :, :]

                # 将图片分成层次
                layers = [
                    np.all(img_section == [28, 28, 28], axis=-1),
                    np.all(img_section == [56, 56, 56], axis=-1),
                    np.all(img_section == [84, 84, 84], axis=-1),
                    np.all(img_section == [112, 112, 112], axis=-1),
                    np.all(img_section == [140, 140, 140], axis=-1),
                    np.all(img_section == [168, 168, 168], axis=-1),
                    np.all(img_section == [196, 196, 196], axis=-1),
                    np.all(img_section == [224, 224, 224], axis=-1),
                    np.all(img_section == [252, 252, 252], axis=-1)
                ]
                # 计算每层的厚度
                for i in range(0, len(layers)):
                    # 找到每层的上边界和下边界
                    top_boundary = np.max(np.where(layers[i], np.indices(layers[i].shape)[0], 0), axis=0)
                    bottom_boundary = np.min(np.where(layers[i], np.indices(layers[i].shape)[0], layers[i].shape[0]), axis=0)
                    thickness = top_boundary - bottom_boundary
                    thickness = thickness[thickness > 0]
                    if len(thickness) > 0:
                        # 将像素厚度转化为实际物理厚度，单位为um
                        thickness_um = np.mean(thickness) * self.pixel_to_um_ratio * self.vertical_scale
                        ALL[i].append(thickness_um)

        dataframe = pd.DataFrame(ALL).T
        save = os.path.join(pic_new_path, '0-6' + ".csv")
        dataframe.to_csv(save, header=True, index_label=self.list_name)


z = remask()
z.msk()
