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

#print(A)
#print(B)

