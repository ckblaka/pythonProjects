rep = 'o'
T = []
VAN = float(0)
### Demande de la saisie du taux
taux = input('Saisir le taux:')
t = float(taux)

### Demande de la saisie de l'investissement I
I = float(input('Saisir l'' investissement:'))

### Demande de la saisie des Cash Flows CF
#while rep == 'o':
    #ch = input('Entrez un cash flow')
    #cf = int(ch)
    #T.append(cf)
    #rep = input('voulez-vous continuer? ')
#print('Les valeurs Saisies ', T)

#T = [200000, 140000, 150000, 250000, 600000]

### Affiche le nombre de cache flows entrés
n = len(T)

### calcul de la van
print('--------- calcul des VAN ---------')
for k in range(n):
    VAN = VAN + T[k]/((1 + t)**(1+k))
VAN = VAN - I
print(VAN)
print('--------- Fin de calcul des VAN ---------')



