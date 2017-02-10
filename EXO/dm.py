## les fonctions de constant
def affiche (c):
    for k in range(len(c)):
        print(c[k])

def sommeDiag2(t):
    affiche(t)
    n = len(t)
    j = 0
    somme = 0
    for i in range(n - 1, -1, -1):
        print(i)
        somme = somme + t[j][i]
        j = j + 1
    return somme

def sommeligne(c,i):
    """ cette fonction renvoie la somme des valeurs de la ligne i de C"""
    a = 0
    b = len(c)
    for k in range(b):
        a = c[i][k] + a
    return a

def somme(L):
    a = 0
    for k in range(len(L)):
        a = a + L[k]
    return a