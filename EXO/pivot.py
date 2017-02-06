def pivot(T,j):
    """cette fonction renvoie le premier coefficient non nul de la colonne j de T à partir de la diagonale"""
    n = len(T[0])
    affiche(T)
    #i=j
    if j >= n:
        print('OutBounds for = ' + str(j))
        return -1
    for k in range(j, n):
        if j == k:
            while T[k][j] == 0:
                k = k + 1
        return k

def reduc(T,j):
    """cette fonction renvoie le premier coefficient non nul de la colonne j de T à partir de la diagonale"""
    lignePivot = pivot(T,j)
    print ('lignePivot ' + str(lignePivot))
    n = len(T[0])
    T0 = []
    for i in range(n):
        if i == lignePivot:
            T0.append([1])
        else:
            # si la ligne dans la colonne  j correspond à celle du pivot alor la valeur = 1
            T0.append([0])
    return T0

def affiche(T):
    """cette fonction affiche T sous forme d'une matrice"""
    for i in range(len(T)):
        print(T[i])
def pivote(T, j):
    """cette fonction renvoie le"""
    affiche(T)
    n = len(T)
    print('Dimension de T = ' + str(n))
    if j >= n:
        print('OutBounds for = ' + str(j))
        return -1
    for k in range(n):
        print('k =' + str(k))
        if j == k:
            #print ('-- j= ' + str(j) + ' k = ' + str(k))
            for m in range(j, n):
                print(str(m) + ',' + str(j) + '=>' + str(T[m][j]))
                #print( '##' + str(T[j][m]))
                if T[m][j] != 0:
                    if m != n:
                        #print ('* ' + str(T[m][j]))
                        res = m
                    else:
                        res = n
                    #print ('resultat' + str(res))
                    return affiche(res)

## exemple avec T=[[0,-1,1,8],[1,3,-1,4],[3,0,0,2],[1,5,2,4]]
## voici les resultats
#T = [[0, -1, 1, 8], [1, 3, -1, 4], [3, 0, 0, 2], [1, 5, 2, 4]]
#B= reduc(T,1)