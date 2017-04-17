import pivot
import dm
T = [[0, -1, 1, 8], [1, 3, -1, 4], [3, 0, 0, 2], [1, 5, 2, 4]]
B = pivot.reduc(T,3)

print('Affiche B')
pivot.affiche(B)
k = dm.sommeligne(T,0)
print('somme = ', k)
print('-----')
g = dm.sommeDiag2(T)

print('-- exection Factorielle --')

a = pivot.facto(9)


