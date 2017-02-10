"""les fonctions de constant"""
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

def sommecolonne(C,j):
    """cette fonction renvoie la somme des valeurs de la colonne j de C"""
    a = 0
    b = len(C[0])
    for k in range(b):
        a = a+C[k][0]
    return a
def sommediag1(C):
    """cette fonction renvoie  somme  valeurs  premiere diagonale de C (d'en haut a gauche a en bas a droite)"""
    a = 0
    b = len(C)
    for k in range(b):
        a = a+C[k][k]
    return a
def sommediag2(C):
    """cette fonction renvoie  somme  valeurs  seconde diagonale de C (d'en bas à gauche à en haut a droite)"""
    a = 0
    b = len(C)
    for k in range(b):
        a = a+C[k][len(C)-1-k]
    return a

def magique(C):
    """cette fonction renvoie un booléen carré magique ou non"""
    b = len(C)
    for k in range(b):
        test = sommeligne(C, k) == sommecolonne(C, k) == sommediag1(C) == sommediag2(C)
    return test
## partie kezia au 10/02/2017 AM