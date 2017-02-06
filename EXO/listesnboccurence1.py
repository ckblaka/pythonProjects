import time

temp = time.clock()
L1=[]
L2=[]
L=['q','s','q','s','a','b','a','b','c','q','a','d']
L2 = list(set(L))
k=0
print(L)
print(L2)
for x in  L2:
    for y in L:
        if x==y:
            k=k+1
    L1.append(x + ':' + str(k))        
    k=0 
dif = time.clock() - temp        
print(L1)
print (dif)
