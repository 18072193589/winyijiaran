import os


class BatchRename():
    '''
    批量重命名文件夹中的图片文件（其他文件也可）
    '''

    def __init__(self):
        self.path = r'D:\Deep-Learing\NetModel\connext\YY_HM_result_dice2\YY_2\8位1024'  # 表示需要命名处理的文件夹

        #self.path2 = r'C:\Users\Administrator\Desktop\data_shuoming\fenkuai\img'  # 表示需要命名处理的文件夹
    def rename(self):
        savedpath = self.path
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 0  # 表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith(('.png','.tif')):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其
                # 他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)

                ps = item.split('.')
                # dst = os.path.join(os.path.abspath(savepath), str(ps[-3]+ps[-2]+ps[-1]))
                #dst = os.path.join(os.p ath.abspath(savedpath), str(i) + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
                #dst = os.path.join(os.path.abspath(self.path), str(ps[0]+ps[1])+ '.png')    #这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
                dst = os.path.join(os.path.abspath(self.path),
                                   str(ps[0]) + '_seg.png')  # 这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()