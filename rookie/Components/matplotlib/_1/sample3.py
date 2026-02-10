import pandas as pd
import numpy as np
import datashader as ds
import datashader.transfer_functions as tf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 生成大规模时间序列数据
n_points = 5000000
print(f"生成 {n_points:,} 个时间序列点...")

# 创建时间序列
start_date = datetime(2020, 1, 1)
dates = [start_date + timedelta(hours=i) for i in range(n_points)]

# 生成多个时间序列（模拟传感器数据）
np.random.seed(42)
base_trend = np.sin(np.linspace(0, 50 * np.pi, n_points))
noise = np.random.normal(0, 0.3, n_points)
trend = np.linspace(0, 10, n_points)

# 创建多个序列
series_data = []
for i in range(5):  # 5个序列
    x = np.array(dates)
    y = base_trend * (1 + i*0.2) + noise * (1 + i*0.1) + trend + i*2
    series_data.append(pd.DataFrame({
        'time': x,
        'value': y,
        'series': f'Series_{i+1}'
    }))

df = pd.concat(series_data, ignore_index=True)

# 使用Datashader聚合时间序列
canvas = ds.Canvas(
    plot_width=1200,
    plot_height=400,
    x_range=(df['time'].min(), df['time'].max())
)

# 按系列分组绘制线
agg = canvas.line(
    df,
    x='time',
    y='value',
    agg=ds.mean('value'),
    line_width=1  # 可选：设置线宽
)

# 应用颜色
img = tf.shade(agg, cmap=plt.cm.plasma, how='eq_hist')

# 背景设置为白色
img_bg = tf.set_background(img, "white")

# 使用matplotlib显示
fig, ax = plt.subplots(figsize=(14, 6))
ax.imshow(img_bg.to_pil(), aspect='auto',
          extent=[df['time'].min().timestamp(),
                  df['time'].max().timestamp(),
                  df['value'].min(),
                  df['value'].max()])

# 设置时间轴格式
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title(f"{n_points:,} 个时间序列点 (5个序列)")

# 优化时间显示
import matplotlib.dates as mdates
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()