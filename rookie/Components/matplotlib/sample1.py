import matplotlib.pyplot as plt
import numpy as np

# 生成500个数据点
x = np.linspace(0, 10, 500)  # 0到10之间的500个点
y = np.sin(x)  # 正弦函数数据

# 创建图形
plt.figure(figsize=(12, 6))
plt.plot(x, y, color='blue', linewidth=1.5, label='Sine Wave')

# 添加标题和标签
plt.title('500个数据点的折线图示例', fontsize=16, fontweight='bold')
plt.xlabel('X轴', fontsize=12)
plt.ylabel('Y轴', fontsize=12)

# 添加网格和图例
plt.grid(True, alpha=0.3)
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()