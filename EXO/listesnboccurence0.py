### Première version  mais prob de perf
import time

temp = time.clock()
L1=[]
x=0
L2=[]
L=['q','s','q','s','a','b','a','b','c','q','a','d']
L2 = list(set(L))
print(L)
print(L2)
for x in L2:
    a=L.count(x)
    d=str(x)
    c= d + ':'+ str(a)
    #print(c)
    L1.append(c)
dif = time.clock() - temp
print(L1)
print (dif)
       
