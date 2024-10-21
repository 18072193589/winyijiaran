import pandas as pd

# 加载两组数据
data1 = pd.read_csv(r'D:\Deep-Learing\NetModel\convnext-U-net\HM_EANET_LOSS1\YY_1\testB\HD\0-6.csv')
data2 = pd.read_csv(r'D:\Deep-Learing\NetModel\convnext-U-net\Ture_data\HM\HD\0-6.csv')

# 计算差值
thickness_diff = data1 - data2

# 计算百分比误差
percentage_error = (thickness_diff / data2)

# 计算百分比误差的均值
mean_percentage_error = percentage_error.mean()


for value in mean_percentage_error.values:
    print(value)

# 保存结果到CSV
#mean_percentage_error.to_csv('thickness_difference_percentage_error_mean.csv')
