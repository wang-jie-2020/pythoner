import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# 生成数据
x = np.linspace(0, 20, 500)

# 创建不同的信号
y_sin = np.sin(x)
y_cos = np.cos(x)
y_sawtooth = signal.sawtooth(2 * np.pi * 0.1 * x)
y_noisy = y_sin + np.random.normal(0, 0.2, 500)

# 创建2x2的子图布局
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('500个数据点的多种信号可视化', fontsize=18, fontweight='bold')

# 子图1：正弦波
axes[0, 0].plot(x, y_sin, color='royalblue', linewidth=2)
axes[0, 0].set_title('正弦波', fontsize=14)
axes[0, 0].set_xlabel('时间')
axes[0, 0].set_ylabel('幅度')
axes[0, 0].grid(True, alpha=0.3)

# 子图2：余弦波
axes[0, 1].plot(x, y_cos, color='crimson', linewidth=2)
axes[0, 1].set_title('余弦波', fontsize=14)
axes[0, 1].set_xlabel('时间')
axes[0, 1].set_ylabel('幅度')
axes[0, 1].grid(True, alpha=0.3)

# 子图3：锯齿波
axes[1, 0].plot(x, y_sawtooth, color='darkgreen', linewidth=2)
axes[1, 0].set_title('锯齿波', fontsize=14)
axes[1, 0].set_xlabel('时间')
axes[1, 0].set_ylabel('幅度')
axes[1, 0].grid(True, alpha=0.3)

# 子图4：含噪声的正弦波
axes[1, 1].plot(x, y_noisy, color='purple', linewidth=1, alpha=0.7)
axes[1, 1].plot(x, y_sin, color='black', linewidth=1.5, linestyle='--', alpha=0.8)
axes[1, 1].set_title('含噪声的正弦波', fontsize=14)
axes[1, 1].set_xlabel('时间')
axes[1, 1].set_ylabel('幅度')
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].legend(['含噪声信号', '原始信号'])

plt.tight_layout()
plt.show()
