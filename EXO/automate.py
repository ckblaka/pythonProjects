import numpy as np
import matplotlib.pyplot as plt
def dessin(T):
    """automate cellulaire 0 rond blanc 1 tond rouge"""
    n=len(T)
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                plt.plot(j, n - 1 - i, 'wo')
            else:
                plt.plot(j, n - 1 - i, 'ro')
    plt.show()
    plt.draw()