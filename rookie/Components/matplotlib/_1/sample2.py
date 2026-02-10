import datashader as ds
import datashader.transfer_functions as tf
from datashader.colors import Sets1to3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 生成带分类的大规模数据
n = 2000000
categories = ['A', 'B', 'C', 'D']

data = []
for i, cat in enumerate(categories):
    n_points = n // len(categories)
    x = np.random.normal(i, 1, n_points)
    y = np.random.normal(i, 1, n_points)
    data.append(pd.DataFrame({
        'x': x,
        'y': y,
        'category': cat
    }))

df = pd.concat(data, ignore_index=True)

# 创建画布
canvas = ds.Canvas(plot_width=800, plot_height=600)

# 按类别聚合
agg = canvas.points(df, 'x', 'y', ds.count_cat('category'))

# 为不同类别分配颜色
color_key = {cat: color for cat, color in zip(categories, Sets1to3)}
img = tf.shade(agg, color_key=color_key, how='eq_hist')

# 转换为matplotlib格式
img_matplotlib = tf.set_background(img, "white")

# 显示
fig, ax = plt.subplots(figsize=(12, 9))
ax.imshow(img_matplotlib.to_pil(), aspect='auto')

# 添加图例
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=cat)
                   for cat, color in color_key.items()]
ax.legend(handles=legend_elements, loc='upper right')

ax.set_title(f"{len(df):,} 个点按类别着色")
ax.axis('off')
plt.show()