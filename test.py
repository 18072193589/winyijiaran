import cv2
import os

img2_path = r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9\testB'
img2_list = os.listdir(img2_path)
img2 = None
for item2 in img2_list:
    if (item2.endswith('.png')):
        src2 = os.path.join(img2_path, item2)
        best_img2 = img2
        best_mmd = 999
        img2 = cv2.imread(src2)