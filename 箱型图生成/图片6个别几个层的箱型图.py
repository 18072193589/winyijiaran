import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体路径 (Windows 系统上)
font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf', size=12)  # 使用黑体字体

# 加载数据
file_path = '箱子图.xlsx'
data = pd.read_excel(file_path)

# 定义每组数据的列名
columns_gcl = ['CE-GCL', 'DICE-GCL', 'CAT-GCL']
columns_hfl = ['CE-HFL', 'DICE-HFL', 'CAT-HFL']
columns_os = ['CE-OS', 'DICE-OS', 'CAT-OS']
columns_choroid = ['CE-CHOROID', 'DICE-CHOROID', 'CAT-CHOROID']

# 创建箱型图
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 设置中文标题
fig.suptitle('CAT-Loss与其他Loss在HM分割厚度误差之间的性能比较', fontproperties=font)

# GCL组数据
axes[0, 0].boxplot(data[columns_gcl].values, labels=columns_gcl)
axes[0, 0].set_title('GCL', fontproperties=font)

# HFL组数据
axes[0, 1].boxplot(data[columns_hfl].values, labels=columns_hfl)
axes[0, 1].set_title('HFL', fontproperties=font)

# OS组数据
axes[1, 0].boxplot(data[columns_os].values, labels=columns_os)
axes[1, 0].set_title('OS', fontproperties=font)

# CHOROID组数据
axes[1, 1].boxplot(data[columns_choroid].values, labels=columns_choroid)
axes[1, 1].set_title('CHOROID', fontproperties=font)

# 调整布局并显示
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
