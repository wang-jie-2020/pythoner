import matplotlib.pyplot as plt
import numpy as np

# 最简单的例子
x = np.arange(500)  # 0到499
y = np.random.randn(500).cumsum()  # 累积随机数

plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('简单的500点折线图')
plt.xlabel('索引')
plt.ylabel('值')
plt.grid(True)
plt.show()