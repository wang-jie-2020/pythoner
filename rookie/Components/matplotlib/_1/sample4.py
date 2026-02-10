import datashader as ds
import pandas as pd
import numpy as np
from datashader import transfer_functions as tf
from datashader.colors import viridis

import bokeh.plotting as bp
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import row, column
from bokeh.models import HoverTool, WheelZoomTool, PanTool, ResetTool

# 在Jupyter中显示
output_notebook()

# 生成数据
n = 3000000
x = np.random.normal(0, 2, n)
y = np.random.normal(0, 2, n)
colors = np.random.choice(['red', 'blue', 'green'], n, p=[0.5, 0.3, 0.2])

df = pd.DataFrame({'x': x, 'y': y, 'color': colors})

# 定义聚合函数
def create_image(x_range, y_range, w=800, h=600):
    """根据范围创建聚合图像"""
    cvs = ds.Canvas(plot_width=w, plot_height=h,
                    x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'x', 'y')
    img = tf.shade(agg, cmap=viridis, how='log')
    return tf.dynspread(img, threshold=0.5, max_px=3)

# 创建Bokeh图表
p = figure(tools='wheel_zoom,pan,reset,hover,save',
           width=800, height=600,
           x_range=(-5, 5), y_range=(-5, 5))

# 初始范围
x_range, y_range = (-5, 5), (-5, 5)
image = create_image(x_range, y_range)

# 将Datashader图像转换为Bokeh可用的格式
p.image_rgba(image=[image.data],
             x=x_range[0], y=y_range[0],
             dw=x_range[1]-x_range[0],
             dh=y_range[1]-y_range[0])

# 添加工具提示
hover = p.select_one(HoverTool)
hover.tooltips = [("位置", "($x, $y)")]

p.title.text = f"交互式大规模数据可视化 ({n:,}个点)"
p.xaxis.axis_label = "X轴"
p.yaxis.axis_label = "Y轴"

# 显示
show(p)