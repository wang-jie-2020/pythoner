import numpy as np
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
from datashader.colors import inferno, viridis
import matplotlib.pyplot as plt
from io import BytesIO
import time

# 生成500万个随机点
num_points = 5000000
print(f"生成 {num_points:,} 个数据点...")

# 方法1: 使用numpy生成正态分布数据
np.random.seed(42)
x = np.random.normal(0, 1, num_points)
y = np.random.normal(0, 1, num_points)

# 添加一些类别信息
categories = np.random.choice(['A', 'B', 'C'], num_points, p=[0.5, 0.3, 0.2])

# 创建DataFrame
df = pd.DataFrame({'x': x, 'y': y, 'category': categories})

print("开始渲染...")
start_time = time.time()

# 创建画布
canvas = ds.Canvas(
    plot_width=800,
    plot_height=600,
    x_range=(-5, 5),  # 可设置固定范围或自动
    y_range=(-5, 5)
)

# 聚合点数据
agg = canvas.points(df, 'x', 'y')

# 应用颜色映射
img = tf.shade(agg, cmap=viridis)
# 或使用动态范围调整
img = tf.shade(agg, cmap=viridis, how='log')

print(f"渲染完成，耗时: {time.time() - start_time:.2f} 秒")

# 转换为matplotlib可显示格式
img_plot = tf.set_background(img, "white")

# 使用matplotlib显示
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(img_plot.to_pil(), aspect='auto')
ax.set_title(f"{num_points:,} 个点的可视化")
ax.axis('off')
plt.tight_layout()
plt.show()