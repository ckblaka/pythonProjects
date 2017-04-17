import time
import numpy as np
import matplotlib.pyplot as plt
def produitMatrice(T1, T2):
    T = []
    if len(T1[0]) != len(T2):
        #print "erreur"
        return False
    for i in range(len(T1)):
        ligne = []
        for j in range(len(T2[0])):
            element = 0
            for k in range(len(T1[0])):
                element = element + T1[i][k] * T2[k][j]
            ligne.append(element)
        T.append(ligne)
    return T

# A = [[2, 3], [4, 5]]  #(n,m)
# B = [[6, 7], [8, 9]]  #(k, p)

start = time.time()
print("hello")
time.sleep(0.3)

zeros = np.zeros((1, 10), np.float64)
print(zeros)

end = time.time()
print(end - start)

