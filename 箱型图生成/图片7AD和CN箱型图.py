from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体路径 (Windows 系统上)
font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf', size=12)  # 使用黑体字体

# 读取数据
ad_data = pd.read_csv('AD12.csv')
cn_data = pd.read_csv('CN12.csv')

# 定义视网膜层
layers = ['RNFL', 'GCL+IPL', 'INL', 'OPL', 'HFL+ONL', 'MEZ', 'OS', 'IZ+PRE', 'CHOROID']

# 创建9宫格图
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
# 设置中文标题
fig.suptitle('Quantitative clinical impact with CAT-LOSS', fontproperties=font)
fig.suptitle('Quantitative clinical impact with CAT-LOSS', fontproperties=font)
# 逐个层次绘制箱型图
for i, ax in enumerate(axes.flatten()):
    # 从三个数据集中提取当前层的厚度数据
    data_to_plot = [
        ad_data[layers[i]].dropna(),
        cn_data[layers[i]].dropna()
    ]
    
    # 绘制箱型图
    ax.boxplot(data_to_plot, labels=['AD', 'CN'])
    ax.set_title(f'{layers[i]} Thickness')
    ax.set_ylabel('')

# 调整布局
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
