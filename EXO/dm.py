## les fonctions
def affiche (c):
    for k in range(len(c[0])):
        print(c[k])

def sommeligne(C,i):
    """ cette fonction renvoie la somme des valeurs de la ligne i de C"""
    a = 0
    b = len(C[0])
    for k in range(b):
        a = C[i][k]+a
        print(a)
    return a

def somme(L):
    a = 0
    for k in range(len(L)):
        a = a+L[k]
    return a