import matplotlib.pyplot as plt
import numpy as np

# 生成500个数据点
np.random.seed(42)  # 设置随机种子确保可重复性
x = np.arange(500)

# 创建三个不同的数据序列
y1 = np.cumsum(np.random.randn(500))  # 随机游走
y2 = 50 + 30 * np.sin(x * 0.05)  # 正弦波
y3 = 100 - 0.2 * x + np.random.randn(500) * 5  # 趋势线加噪声

# 创建图形
plt.figure(figsize=(14, 7))

# 绘制三条折线
plt.plot(x, y1, label='随机游走', color='red', linewidth=1.5, alpha=0.8)
plt.plot(x, y2, label='正弦波', color='green', linewidth=1.5, alpha=0.8)
plt.plot(x, y3, label='趋势线', color='blue', linewidth=1.5, alpha=0.8)

# 自定义图表
plt.title('多个数据序列的折线图', fontsize=16, pad=20)
plt.xlabel('数据点索引', fontsize=12)
plt.ylabel('数值', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=10)
plt.xlim(0, 500)

# 添加背景色
plt.axhspan(-50, 50, alpha=0.1, color='gray')

plt.tight_layout()
plt.show()