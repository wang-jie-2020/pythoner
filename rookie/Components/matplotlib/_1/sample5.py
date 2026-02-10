import holoviews as hv
from holoviews.operation.datashader import datashade, dynspread
import numpy as np
import pandas as pd

hv.extension('bokeh')

# 生成大数据
n = 5000000
x = np.random.randn(n)
y = np.random.randn(n)
df = pd.DataFrame({'x': x, 'y': y})

# 创建Holoviews点对象
points = hv.Points(df, ['x', 'y'])

# 使用Datashader动态渲染
shaded = datashade(points, cmap='viridis', width=800, height=600)
spreaded = dynspread(shaded, threshold=0.5, max_px=3)

# 添加交互控件
from holoviews.plotting.links import RangeToolLink
from holoviews import streams

# 创建交互式图表
plot = spreaded.opts(
    title=f"{n:,} 个点的动态可视化",
    xlabel="X",
    ylabel="Y",
    tools=['hover', 'wheel_zoom', 'pan', 'reset']
)

# 保存为HTML或显示
hv.save(plot, 'large_data_viz.html')
# 或在Jupyter中显示
# hv.render(plot)