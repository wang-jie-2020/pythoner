import plotly.graph_objects as go
import numpy as np

# 生成数据
x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# 创建交互式图表
fig = go.Figure()

# 添加三条轨迹
fig.add_trace(go.Scatter(
    x=x, y=y1,
    mode='lines',
    name='sin(x)',
    line=dict(color='firebrick', width=2)
))

fig.add_trace(go.Scatter(
    x=x, y=y2,
    mode='lines',
    name='cos(x)',
    line=dict(color='royalblue', width=2)
))

fig.add_trace(go.Scatter(
    x=x, y=y3,
    mode='lines',
    name='sin(x)*cos(x)',
    line=dict(color='green', width=2, dash='dash')
))

# 更新布局
fig.update_layout(
    title='交互式折线图 - 500个数据点',
    xaxis_title='X轴',
    yaxis_title='Y轴',
    hovermode='x unified',
    template='plotly_white',
    height=600
)

# 显示图表
fig.show()