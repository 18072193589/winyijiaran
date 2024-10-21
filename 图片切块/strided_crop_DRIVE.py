from PIL import Image
import numpy as np
import os
import cv2
class fenkuai():
    def strided_crop(self):
        # path=r'D:\Deep-Learing\NetModel\ganseg-master2.0\ganseg-master\dataset\hdb_to_oil_canon_nogan_block\trainB\\'
        path=r'C:\TZBdata\AfterMask\mask\alter'
        filelist = os.listdir(path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        height=512
        width=512
        stride=2000
        BLACK = [0,0,0]
        H=600#微调，向下加?个像素
        P=0#同理
        name=""#文件后缀名
        pic_new_path = os.path.join(path, "alter")
        if not os.path.exists(pic_new_path):
            os.makedirs(pic_new_path)
            #print("max_x:",max_x)
        #print("max_y:",max_y)
        # max_crops = (max_x)*(max_y)
        i = 0
        for item in filelist:
            if item.endswith('.png'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                img_name = os.path.join(path,item)
                img = cv2.imread(img_name)
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #img = Image.open(img_name)
                cv_img = cv2.copyMakeBorder(img,0,0,0,1,cv2.BORDER_CONSTANT, value=BLACK)
                im = np.asarray(cv_img)
                max_x = int(((im.shape[0] - height) / stride) + 1)
                max_y = int(((im.shape[1] - width) / stride) + 1)
                for h in range(max_x):
                    for w in range(max_y):
                            crop_img_arr = im[h * stride+H:(h * stride) + height+H,w * stride + P:(w * stride) + width + P]
                            #print(crop_img_arr.shape)
                            crop_img = Image.fromarray(crop_img_arr)
                            # img_name = directories[1] + "/" + name + "_" + str(i+1)+".png"
                            dst = os.path.join(pic_new_path, '00' + format(str(i), '0>3s')+name + '_seg.png')
                            crop_img.save(dst)
                            i = i + 1
                            print(i)

if __name__ == "__main__":

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input_dim', type=int, default=256)
    # parser.add_argument('--stride', type=int, default=256)
    # args = parser.parse_args()
    fk = fenkuai()
    fk.strided_crop()