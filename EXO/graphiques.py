import numpy as np
x=np.linspace(-10,10,20)
y=[sin(t) for t in x]
plt.plot(x,y)
plt.show


def divp(n):
    L=[]
    for k in range (2,n):
        if n%k==0:
            L.apppend(k)
    return L