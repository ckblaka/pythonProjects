""" retourne pour chaque élément de la liste L le nombre d'occurence"""
L1 = []
L=['a', 'c', 'a', 'c', 'b', 'b', 'b', 'a']
while L!=[]:
    for x in range(len(L)):
        a=L.count(L[x])
        d=str(L[x])
        c= d + ':'+ str(a)
        print(c)
        L1.append(c)
        L.remove(L[x])
