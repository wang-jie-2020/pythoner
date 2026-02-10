import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import time

print("\n开始使用LineCollection优化绘制...")
start_time = time.time()

# 生成测试数据
n_points = 5_000_000
x = np.linspace(0, 100, n_points)
y = np.sin(x * 2) * np.cos(x * 0.5) + np.random.normal(0, 0.1, n_points)

# 创建图形
fig, ax = plt.subplots(figsize=(20, 10))

# 使用LineCollection - 对于大量线段更高效
# 将数据分成多个段
n_segments = 1000
segment_size = n_points // n_segments

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# 只创建LineCollection，不设置颜色映射
lc = LineCollection(segments,
                    colors='blue',
                    linewidths=0.05,  # 非常细的线
                    alpha=0.3,        # 半透明
                    capstyle='round')

ax.add_collection(lc)

# 设置坐标轴范围
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() - 0.1, y.max() + 0.1)

# 添加标题和标签
ax.set_title(f'LineCollection绘制500万数据点', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)
ax.grid(True, alpha=0.1, linewidth=0.3)

# 添加统计信息
stats_text = (f'总数据点: {n_points:,}\n'
              f'线段数量: {len(segments):,}\n'
              f'X范围: [{x.min():.2f}, {x.max():.2f}]\n'
              f'Y范围: [{y.min():.4f}, {y.max():.4f}]')
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# 保存图片
output_path = '5m_points_linecollection.png'
print(f"保存LineCollection图片到: {output_path}")
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)

end_time = time.time()
print(f"LineCollection绘制完成! 耗时: {end_time - start_time:.2f} 秒")