import time

temp = time.clock()
c = ''
L = []
d = 0
texte = 'patagggtetoyyoyoyoyoyoyoooyoyoyoyoyoyoyss'
for i in texte:
    if i not in c:
        c = c+i
for j in c:
    for i in texte:
        if j == i:
            d = d+1
    L.append(d)
    d = 0

max = 0

for i in range(len(L)):
    if L[i]>max:
        max = L[i]
        indix = i
print(L)
print(c)
print(texte)
print( c[indix] + ' apparait '+ str(max) + ' fois') 



