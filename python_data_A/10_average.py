import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

print(y2)

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (10,8))

axes[0, 0].plot(x, y1, label = 'sin(x)', color = 'blue')
axes[0, 0].set_title('Line Plot 1')
axes[0, 0].legend()

axes[0, 1].plot(x, y2, label = 'cos(x)', color = 'orange')
axes[0, 1].set_title('Line Plot 2')
axes[0, 1].legend()

axes[1, 0].plot(x, y3, label = 'tan(x)', color = 'green')
axes[1, 0].set_title('Line Plot 3')
axes[1, 0].legend()

axes[1, 1].plot(x, y4, label = 'exp(-x)', color = 'red')
axes[1, 1].set_title('Line Plot 4')
# axes[1, 1].legend()

plt.tight_layout()

plt.show()