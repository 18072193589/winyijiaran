from PIL import Image
import os
import cv2
##NEAREST 灰度延申，不增加额外的灰度值
class zsjpre():
    def repre(self):
        file_path = r"D:\Deep-Learing\DP-Data\一磊老师数据\筛选后的图"    # 原始图像路径

        raw_files = os.walk(file_path)              # 遍历所有图像
        width, height = 1024, 1024                    # 修改后的图像尺寸大小

        # 28 56 84 112 140 168 196 224 252
        current_file = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file)
        for root, dirs, files in raw_files:
            for file in files:                      # 展现各文件
                if file.endswith('.png') and not file.endswith('_N.png'):
                    picture_path = os.path.join(root, file)    # 得到图像的绝对路径
                    pic_org = Image.open(picture_path)               # 打开图像
                    pic_org = pic_org.convert('L')
                    pic_new = pic_org.resize((width, height), Image.NEAREST)   # 图像尺寸修改
                    _, sub_folder = os.path.split(root)              # 得到子文件夹名字
                    pic_new_path = os.path.join(file_path, "alter22")
                    if not os.path.exists(pic_new_path):
                        os.makedirs(pic_new_path)                    # 建立子文件夹
                    dst = os.path.join(os.path.abspath(pic_new_path), file)
                    pic_new_path = os.path.join(pic_new_path, dst)  # 新图像存储绝对路径
                    pic_new.save(pic_new_path)					     # 存储文件
                    # img = cv2.imread(pic_new_path)
                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # pic_new_path = os.path.join(current_directory,"LY_9_5_result5\LY_9_5\\testB",file)
                    # if not os.path.exists(pic_new_path):
                    #     os.makedirs(pic_new_path)
                    # cv2.imwrite(pic_new_path, img)
                    print("%s have been resized!" %pic_new_path)
z = zsjpre()
z.repre()