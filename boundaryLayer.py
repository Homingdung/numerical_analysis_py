# boundary layer theory

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
epsilon_1 = 0.01
epsilon_2 = 0.025
epsilon_3 = 0.1
y1 = (np.exp(-x) - np.exp(-x / epsilon_1)) / (np.exp(-1) - np.exp(-1 / epsilon_1))
y2 = (np.exp(-x) - np.exp(-x / epsilon_2)) / (np.exp(-1) - np.exp(-1 / epsilon_2))
y3 = (np.exp(-x) - np.exp(-x / epsilon_3)) / (np.exp(-1) - np.exp(-1 / epsilon_3))

plt.plot(x, y1, label="$\epsilon = 0.01$")
plt.plot(x, y2, label="$\epsilon = 0.025$")
plt.plot(x, y3, label="$\epsilon = 0.025$")
plt.title("Solution plot")
plt.xlabel("x")
plt.legend(loc="upper right")
plt.show()
