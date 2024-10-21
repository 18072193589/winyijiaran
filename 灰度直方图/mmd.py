import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, exposure, img_as_float


def guassian_kernel(source, target):
    '''
    将源域数据和目标域数据转化为核矩阵，即上文中的K
    Params:
     source: (b1,n)的X分布样本数组
     target:（b2，n)的Y分布样本数组
    Return:
      kernel_val: 对应的核矩阵
    '''
    # 堆叠两组样本，上面是X分布样本，下面是Y分布样本，得到（b1+b2,n）组总样本
    n_samples = source.shape[0]+target.shape[0]
    total = np.concatenate((source, target), axis=0)
    # 对总样本变换格式为（1,b1+b2,n）,然后将后两维度数据复制到新拓展的维度上（b1+b2，b1+b2,n），相当于按行复制
    total0 = np.expand_dims(total,axis=0)
    total0= np.broadcast_to(total0,[(total.shape[0]), (total.shape[0]), (total.shape[1])])
    # 对总样本变换格式为（b1+b2,1,n）,然后将后两维度数据复制到新拓展的维度上（b1+b2，b1+b2,n），相当于按复制
    total1 = np.expand_dims(total,axis=1)
    total1=np.broadcast_to(total1,[(total.shape[0]), (total.shape[0]), (total.shape[1])])
    # total1 - total2 得到的矩阵中坐标（i,j, :）代表total中第i行数据和第j行数据之间的差
    # sum函数，对第三维进行求和，即平方后再求和，获得高斯核指数部分的分子，是L2范数的平方
    L2_distance_square = np.cumsum(np.square(total0-total1),axis=2)
    #调整高斯核函数的sigma值
    bandwidth = np.sum(L2_distance_square) / (n_samples**2-n_samples)
    #高斯核函数的数学表达式
    kernel_val = np.exp(-L2_distance_square / bandwidth)
    #得到最终的核矩阵
    return kernel_val

def MMD(source, target):
    '''
    计算源域数据和目标域数据的MMD距离
    Params:
     source: 源域数据，行表示样本数目，列表示样本数据维度
     target: 目标域数据 同source
    Return:
     loss: MMD loss
    '''
    batch_size = source.shape[0]#一般默认为X和Y传入的样本的总批次样本数是一致的
    kernels = guassian_kernel(source, target)
    #将核矩阵分成4部分
    loss = 0
    for i in range(batch_size):
        s1, s2 = i, (i + 1) % batch_size
        t1, t2 = s1 + batch_size, s2 + batch_size
        loss += kernels[s1, s2] + kernels[t1, t2]
        loss -= kernels[s1, t2] + kernels[s2, t1]
    # 这里计算出的n_loss是每个维度上的MMD距离，一般还会做均值化处理
    n_loss= loss / float(batch_size)
    return np.mean(n_loss)
img1 = cv2.imread(r'D:\Deep-Learing\NetModel\GANSEG5.0\dataset\ALL_revue_to_SW-9\testA\00001.png')#原域
img2_ = cv2.imread(r'D:\Deep-Learing\DP-Data\matlab-retina\5朱绅聚\HDB\DV14LW_02\linw000.jpg')#目标域
hist = cv2.calcHist([img1], [0], None, [256], [0, 255])
best_mmd=999
best_img2 = img2_
best_t = 0
for t in range (3,30):
    img2 = img2_
    img2 = exposure.adjust_gamma(img2, t / 10)
    #计算灰度变换的直方图
    hist_res = cv2.calcHist([img2], [0], None, [256], [0,255])
    now = MMD(hist,hist_res)
    if now<best_mmd:
        best_mmd = now
        best_img2 = img2
        best_t = t
    print("当前MMD{0}".format(now))
print("最优MMD：{0},最优gamma值：{1}".format(best_mmd,best_t))

