import pandas as pd

# 加载两组数据
data1 = pd.read_csv(r'D:\Deep-Learing\NetModel\convnext-U-net\CN_UNET_CE\YY_CN_1\testB\HD\0-6.csv')

# 计算差值
thickness = data1



# 计算均值
mean_percentage = thickness.mean()

# 打印结果
print(mean_percentage)


# 保存结果到CSV
#mean_percentage_error.to_csv('thickness_difference_percentage_error_mean.csv')
