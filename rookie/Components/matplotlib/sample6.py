import matplotlib.pyplot as plt
import numpy as np
import time
import os

# 设置中文字体支持（如果需要）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 生成500万数据点
print("生成数据...")
np.random.seed(42)
n_points = 5_000_000
x = np.linspace(0, 100, n_points)

# 创建复杂信号
y = (np.sin(x) * 0.5 +
     np.sin(x * 3) * 0.3 +
     np.sin(x * 10) * 0.1 +
     np.random.normal(0, 0.05, n_points))

print(f"数据点数量: {n_points:,}")
print(f"数据大小: {x.nbytes + y.nbytes:,} 字节 ({((x.nbytes + y.nbytes) / (1024 ** 3)):.2f} GB)")

# 方法1A: 完整折线图
print("\n开始绘制完整折线图...")
start_time = time.time()

fig, ax = plt.subplots(figsize=(16, 8))

# 使用较细的线条和合适的alpha值
line = ax.plot(x, y,
               color='blue',
               linewidth=0.1,  # 非常细的线
               alpha=0.5,  # 半透明
               solid_capstyle='round')[0]

ax.set_title(f'500万数据点完整折线图 (无采样)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)
ax.grid(True, alpha=0.1, linewidth=0.5)

# 设置合适的坐标轴范围
ax.set_xlim(x[0], x[-1])

# 添加数据统计信息
stats_text = f'数据点: {n_points:,}\n均值: {y.mean():.4f}\n标准差: {y.std():.4f}\n范围: [{y.min():.4f}, {y.max():.4f}]'
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# 保存图片
output_path = '5m_points_full_line.png'
print(f"保存图片到: {output_path}")
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)

end_time = time.time()
print(f"绘制完成! 耗时: {end_time - start_time:.2f} 秒")

# 方法1B: 分区段绘制（提高渲染速度）
print("\n开始分区段绘制...")
start_time = time.time()

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle(f'500万数据点分区段详细视图 (无采样)', fontsize=18, fontweight='bold')

# 定义四个区段
segments = [
    (0, n_points // 4, "前25%数据"),
    (n_points // 4, n_points // 2, "25%-50%数据"),
    (n_points // 2, 3 * n_points // 4, "50%-75%数据"),
    (3 * n_points // 4, n_points, "后25%数据")
]

for idx, (start, end, title) in enumerate(segments):
    row = idx // 2
    col = idx % 2

    x_seg = x[start:end]
    y_seg = y[start:end]

    axes[row, col].plot(x_seg, y_seg,
                        color='darkblue',
                        linewidth=0.1,
                        alpha=0.7)

    axes[row, col].set_title(f'{title} ({len(x_seg):,}个点)', fontsize=12)
    axes[row, col].set_xlabel('X', fontsize=10)
    axes[row, col].set_ylabel('Y', fontsize=10)
    axes[row, col].grid(True, alpha=0.2, linewidth=0.3)

    # 显示该区段的统计信息
    seg_stats = (f'点数: {len(x_seg):,}\n'
                 f'均值: {y_seg.mean():.4f}\n'
                 f'极差: {y_seg.ptp():.4f}')
    axes[row, col].text(0.02, 0.98, seg_stats,
                        transform=axes[row, col].transAxes,
                        fontsize=8, verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# 保存分区段图片
output_path = '5m_points_segments.png'
print(f"保存分区段图片到: {output_path}")
plt.tight_layout(rect=[0, 0, 1, 0.96])  # 为标题留出空间
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)

end_time = time.time()
print(f"分区段绘制完成! 耗时: {end_time - start_time:.2f} 秒")