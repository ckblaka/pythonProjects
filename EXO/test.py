import numpy as np
import matplotlib.pyplot as plt
T = [[0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 0]]
n = len(T)
for i in range(n):
    for j in range(n):
        if T[i][j] == 0:
            plt.plot(j, n - 1 - i, 'bo')
        else:
            plt.plot(j, n - 1 - i, 'ro')
plt.show()
plt.draw()
