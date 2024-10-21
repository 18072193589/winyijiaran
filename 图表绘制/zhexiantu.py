import matplotlib.pyplot as plt

# 假设您有两个网络的Dice系数数据，分别存储在列表 network1_dice 和 network2_dice 中
network1_dice = [0.811,0.817,0.739,0.666,0.811,0.734,0.778,0.705,0.861]
network2_dice = [0.851,0.861,0.756,0.685,0.842,0.745,0.808,0.730,0.916]

# 创建x轴标签，表示十个层级
layers = ['RNFL','GCL+IPL','INL','OPL','HFL+ONL','MEZ','OS','RPE','CHOROID']

# 设置每个网络的折线图
plt.plot(layers, network1_dice, marker='o', label='Convnet')
plt.plot(layers, network2_dice, marker='o', label='U-net')

# 添加标签和标题
plt.xlabel('Layers')
plt.ylabel('Dice Coefficient')
plt.title('Comparison of Dice Coefficients by Layer')
plt.legend()

# 展示图形
plt.xticks(rotation=45)  # 使x轴标签垂直显示
plt.grid(True)  # 添加网格线
plt.tight_layout()  # 确保标签不会重叠
plt.show()