import matplotlib.pyplot as plt
import numpy as np
import time

print("\n开始使用低级别API绘制...")
start_time = time.time()

# 生成数据
n_points = 5_000_000
x = np.linspace(0, 50, n_points)
y = np.exp(-0.1 * x) * np.sin(x * 2) + np.random.normal(0, 0.05, n_points)

# 使用Figure和Axes的低级方法
fig = plt.figure(figsize=(20, 8), dpi=100)
ax = fig.add_subplot(111)

# 直接使用plot，但设置优化参数
line, = ax.plot(x, y,
                '-',           # 实线
                color='darkred',
                linewidth=0.05,
                alpha=0.6,
                solid_capstyle='round',
                solid_joinstyle='round')

# 优化渲染
ax.set_autoscale_on(True)
ax.autoscale_view(tight=True)

# 设置标题和标签
ax.set_title(f'低级别API绘制500万数据点', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('X轴 (时间/索引)', fontsize=12)
ax.set_ylabel('Y轴 (数值)', fontsize=12)

# 添加网格（非常淡）
ax.grid(True, which='both', alpha=0.05, linewidth=0.2)

# 添加统计信息框
import matplotlib.patches as mpatches
stats_text = (f'总点数: {n_points:,}\n'
              f'数据范围: [{x.min():.2f}, {x.max():.2f}]×[{y.min():.4f}, {y.max():.4f}]\n'
              f'均值: {y.mean():.4f} ± {y.std():.4f}')
patch = mpatches.FancyBboxPatch((0.02, 0.92), 0.25, 0.08,
                                boxstyle="round,pad=0.02",
                                transform=ax.transAxes,
                                facecolor='lightgray',
                                alpha=0.8,
                                edgecolor='black',
                                linewidth=0.5)
ax.add_patch(patch)
ax.text(0.03, 0.94, stats_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top')

# 保存为高质量图片
output_path = '5m_points_lowlevel.png'
print(f"保存低级别API图片到: {output_path}")

# 使用更高效的保存选项
plt.savefig(output_path,
           dpi=200,
           bbox_inches='tight',
           facecolor='white',
           edgecolor='none',
           pil_kwargs={'compress_level': 1})

plt.close(fig)

end_time = time.time()
print(f"低级别API绘制完成! 耗时: {end_time - start_time:.2f} 秒")