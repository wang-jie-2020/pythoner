import matplotlib.pyplot as plt
import numpy as np
import time
import os
from datetime import datetime


def plot_large_dataset(x, y, title="大数据集", output_path=None,
                       linewidth=0.1, alpha=0.5, color='blue',
                       figsize=(16, 8), dpi=150):
    """
    绘制大数据集的专用函数

    参数:
    x, y: 数据数组
    title: 图表标题
    output_path: 输出文件路径
    linewidth: 线条宽度
    alpha: 透明度
    color: 线条颜色
    figsize: 图形尺寸
    dpi: 分辨率
    """

    print(f"开始绘制 {len(x):,} 个数据点...")
    start_time = time.time()

    # 创建图形
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    # 绘制折线
    ax.plot(x, y,
            color=color,
            linewidth=linewidth,
            alpha=alpha,
            solid_capstyle='round')

    # 设置标题和标签
    ax.set_title(f'{title} ({len(x):,}个数据点)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('X轴', fontsize=11)
    ax.set_ylabel('Y轴', fontsize=11)

    # 添加网格
    ax.grid(True, alpha=0.1, linewidth=0.3)

    # 添加统计信息
    stats_text = (f'生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                  f'数据点数: {len(x):,}\n'
                  f'X范围: [{x.min():.4f}, {x.max():.4f}]\n'
                  f'Y范围: [{y.min():.4f}, {y.max():.4f}]\n'
                  f'Y均值: {y.mean():.4f} ± {y.std():.4f}')

    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 自动生成输出路径
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f'large_dataset_{len(x)}_{timestamp}.png'

    # 保存图片
    print(f"保存图片到: {output_path}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"绘制完成! 总耗时: {elapsed:.2f}秒")
    print(f"平均速度: {len(x) / elapsed:,.0f} 点/秒")

    # 返回文件信息
    file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
    return {
        'output_path': output_path,
        'file_size_mb': file_size,
        'elapsed_time': elapsed,
        'points_per_second': len(x) / elapsed
    }


# 使用示例
if __name__ == "__main__":
    # 生成500万数据点
    n_points = 5_000_000
    print(f"生成 {n_points:,} 个测试数据点...")

    x = np.linspace(0, 100, n_points)
    y = np.sin(x) * np.cos(x * 0.5) + np.random.normal(0, 0.1, n_points)

    # 绘制并保存
    result = plot_large_dataset(
        x, y,
        title="500万数据点测试",
        color='darkgreen',
        linewidth=0.08,
        alpha=0.6,
        dpi=120  # 降低DPI以减少文件大小
    )

    print(f"\n结果摘要:")
    print(f"  输出文件: {result['output_path']}")
    print(f"  文件大小: {result['file_size_mb']:.2f} MB")
    print(f"  绘制时间: {result['elapsed_time']:.2f}秒")
    print(f"  处理速度: {result['points_per_second']:,.0f} 点/秒")