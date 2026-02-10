"""
完整的大数据可视化工作流程
1. 数据生成/加载
2. 预处理和采样
3. Datashader渲染
4. Matplotlib展示
5. 保存结果
"""

import numpy as np
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
import matplotlib.pyplot as plt
from datetime import datetime
import time


class LargeDataVisualizer:
    def __init__(self, width=1200, height=800):
        self.width = width
        self.height = height
        self.figsize = (width / 100, height / 100)

    def generate_data(self, n_points=5000000):
        """生成示例数据"""
        print(f"生成 {n_points:,} 个数据点...")

        np.random.seed(42)

        # 生成时间序列
        dates = pd.date_range('2020-01-01', periods=n_points, freq='H')

        # 生成多个信号
        t = np.linspace(0, 100, n_points)
        signal1 = np.sin(t) + np.random.normal(0, 0.1, n_points)
        signal2 = np.cos(t * 0.5) + np.random.normal(0, 0.2, n_points)
        signal3 = np.sin(t * 2) * np.cos(t * 0.3) + np.random.normal(0, 0.15, n_points)

        # 创建DataFrame
        df = pd.DataFrame({
            'timestamp': dates,
            'signal1': signal1,
            'signal2': signal2,
            'signal3': signal3,
            'category': np.random.choice(['A', 'B', 'C'], n_points)
        })

        return df

    def render_with_datashader(self, df, x_col, y_col, agg_func='mean'):
        """使用Datashader渲染"""
        start_time = time.time()

        # 创建画布
        canvas = ds.Canvas(
            plot_width=self.width,
            plot_height=self.height,
            x_range=(df[x_col].min(), df[x_col].max())
        )

        # 选择聚合函数
        if agg_func == 'mean':
            reducer = ds.mean(y_col)
        elif agg_func == 'sum':
            reducer = ds.sum(y_col)
        elif agg_func == 'count':
            reducer = ds.count()
        else:
            reducer = ds.mean(y_col)

        # 执行聚合
        agg = canvas.line(df, x=x_col, y=y_col, agg=reducer)

        # 应用颜色
        img = tf.shade(agg, cmap=plt.cm.viridis, how='eq_hist')

        print(f"渲染完成，耗时: {time.time() - start_time:.2f} 秒")
        return img

    def plot_with_matplotlib(self, img, title="大规模数据可视化"):
        """使用Matplotlib显示结果"""
        fig, ax = plt.subplots(figsize=self.figsize)

        # 设置背景为白色
        img_bg = tf.set_background(img, "white")

        # 转换为PIL图像并显示
        ax.imshow(img_bg.to_pil(), aspect='auto')

        # 添加标题和装饰
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.axis('off')

        # 添加信息文本
        info_text = f"数据点: {len(df):,}\n渲染分辨率: {self.width}×{self.height}"
        ax.text(0.02, 0.98, info_text,
                transform=ax.transAxes,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.tight_layout()
        return fig, ax

    def save_high_resolution(self, img, filename, dpi=300):
        """保存高分辨率图像"""
        img_bg = tf.set_background(img, "white")
        pil_img = img_bg.to_pil()

        # 保存为PNG
        pil_img.save(filename, dpi=(dpi, dpi))
        print(f"图像已保存到: {filename}")


# 使用示例
if __name__ == "__main__":
    # 创建可视化器
    viz = LargeDataVisualizer(width=1600, height=900)

    # 生成数据（或加载实际数据）
    df = viz.generate_data(n_points=5000000)

    # 渲染每个信号
    signals = ['signal1', 'signal2', 'signal3']
    fig, axes = plt.subplots(len(signals), 1, figsize=(16, 12))

    for i, signal in enumerate(signals):
        print(f"\n渲染 {signal}...")
        img = viz.render_with_datashader(df, 'timestamp', signal)
        img_bg = tf.set_background(img, "white")

        axes[i].imshow(img_bg.to_pil(), aspect='auto')
        axes[i].set_title(f'{signal} - {len(df):,} 个点', fontsize=14)
        axes[i].axis('off')

    plt.suptitle('500万点时间序列可视化', fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.savefig('large_scale_timeseries.png', dpi=300, bbox_inches='tight')
    plt.show()