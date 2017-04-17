def premier(n):
    """cette fonction indique si le nombre n est premier"""
    if n<=1:
        return False
    for k in range (2,n):
        if n%k==0:
            return False
    return True

def produit(L):
    """cette fonction renvoie le produit des termes de L"""
    p=1
    for k in L:
        p=p*k
    return p

def ecart(L):
    """cette fonction renvoie l'écart max entre deux termes consecutifs de L"""
    L1=[]
    if len(L)>=2:
        for k in range (len(L)-1):
            a = L[k+1]-L[k]
            L1.append(a)
            max=L1[0]
            for i in range(len(L1)):
                if L1[i] > max :
                    max = L1[i]
    return [max,L[k-1],L[k]]


def divp(n):
    """cette fonction renvoie la liste des diviseurs propres et premiers de n"""
    L=[]
    for k in range (1,n):
        if n%k==0 and premier(k)==True:
            L.append(k)
    return (L)

def semip(n):
    """cette fnction indiqude si n est un entier semi-premier"""
    L=divp(n)
    if len(L)!=2 or produit (L)!=n:
        return False
    return True


k=0
while semip(k)==False or semip(k+1)== False or semip(k+2)==False:
    k=k+1
print (k,k+1,k+2)


M=[]
for k in range (2,1000):
    if semip(k)==True:
        M.append(k)
print(M, ecart(M))



