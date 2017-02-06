def facto(n):
    """renvoie pour n, n! qui correspond a p"""
    p=1
    for k in range (1, n+1):
        p=p*k
    return p
    
def nb_chiffres(n):
    """renvoie le nombre de chiffres de n entier nat"""
    L=str(n)
    nb_chiffres=len(L)
    return nb_chiffres
    
def nbb_chiffres(n):
    """renvoie nb de chiffres, de n un entier naturel"""
    c=0
    a=n/10 
    while a > 0.10:
        c=c+1
        print(c)
    return c
    
    