import math

import numpy as np
from sklearn.metrics import confusion_matrix
import cv2
import os
label_path=(r'D:\Deep-Learing\DP-Data\HW\ZCR\mask5'
            r'')
#label = label.reshape(-1)
pred_path=(r'D:\Deep-Learing\NetModel\connext\zc_result5\zc_5\testB')
#pred = pred.reshape(-1)

class zsj():
    def miou(self,label_path,pred_path,long):
        filelist_pre = os.listdir(pred_path)  # 获取文件路径
        filelist_lable = os.listdir(label_path)
        miou_sum=0
        cc=[]
        miou_sums = [0,0,0,0,0,0,0,0,0]
        total_num = len(filelist_pre)  # 获取文件长度（个数）
        start=0
        for t in range(start, long+start+2000):
            p1=0

            p2=0
            for item_pre in filelist_pre:
                if item_pre.startswith('testB_00' + format(str(t), '0>3s') + '_pred.png') :  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                    p1=1
                    pred = cv2.imread(os.path.join(pred_path, item_pre))
                    pred = pred.reshape(-1)
                    break
            for item_lable in filelist_lable:
                if item_lable.startswith('00' + format(str(t), '0>3s') + '_seg.png') :  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                    p2=1
                    lable = cv2.imread(os.path.join(label_path, item_lable))
                    lable = lable.reshape(-1)
                    break
            if(p1==1 and p2==1):
                out = confusion_matrix(lable, pred, labels=[28, 56, 84, 112, 140, 168, 196, 224,252])
                print(out)
                TP = out[0][0]
                FN = out[0][1] + out[0][2]
                FP = out[1][0] + out[2][0]
                TN = out[1][1] + out[1][2] + out[2][1] + out[2][2]
                r, l = out.shape
                print(r, l)
                confuse_temp = np.zeros((2, 2))
                iou_temp = 0
                for i in range(r):
                    TP = out[i][i]
                    temp = np.concatenate((out[0:i, :], out[i + 1:, :]), axis=0)
                    sum_one = np.sum(temp, axis=0)
                    # sum_one = np.expand_dims(sum_one,axis=0)
                    FP = sum_one[i]
                    temp2 = np.concatenate((out[:, 0:i], out[:, i + 1:]), axis=1)
                    FN = np.sum(temp2, axis=1)[i]
                    TN = temp2.reshape(-1).sum() - FN
                    dc = (TP / (TP + FP + FN))
                    if(math.isnan(dc) or dc == 0.0):
                        # print("{0}文件异常".format(item_pre))
                        # cc.append(t)
                        continue
                    iou_temp += dc
                    print("第{0}层：{1}".format(i,dc))
                    miou_sums[i] = miou_sums[i]+dc
                if(iou_temp/r<0.4):
                    cc.append(t)
                miou_sum=miou_sum+(iou_temp / r)
                print((iou_temp / r),t)
        print("例外的预测")
        print(cc)
        print("九层结果")
        for i in range(9):
            print(miou_sums[i]/long)
        return miou_sum/long
if __name__ == '__main__':
    relight = zsj()
    print("平均MiOU:{0}".format(relight.miou(label_path=label_path,pred_path=pred_path,long=161)))