import matplotlib.pyplot as plt

# 假设您有两个网络的Dice系数数据，分别存储在列表 network1_dice 和 network2_dice 中
network1_dice = [0.826,0.869,0.781,0.701,0.864,0.773,0.83,0.747,0.895]
network2_dice = [0.850,0.889,0.822,0.754,0.881,0.804,0.858,0.799,0.904]

# 创建x轴标签，表示十个层级
layers = ['RNFL','GCL+IPL','INL','OPL','HFL+ONL','MEZ','OS','RPE','CHOROID']

# 设置柱状图的宽度
bar_width = 0.35

# 设置每个柱状图的位置
index = range(len(layers))

for i, (x1, x2) in enumerate(zip(index, [i + bar_width for i in index])):
    plt.text(x1, network1_dice[i], str(network1_dice[i]), ha='center', va='bottom')
    plt.text(x2, network2_dice[i], str(network2_dice[i]), ha='center', va='bottom')
# 绘制柱状图
plt.bar(index, network1_dice, bar_width, label='U-NET HM SW')
plt.bar([i + bar_width for i in index], network2_dice, bar_width, label='SWIM  HM SW')

# 添加标签和标题
plt.xlabel('Layers')
plt.ylabel('Dice Coefficient')
plt.title('Comparison of Dice Coefficients by Layer')
plt.xticks([i + bar_width / 2 for i in index], layers)
plt.legend()

# 展示图形
plt.tight_layout()  # 确保标签不会重叠
plt.show()