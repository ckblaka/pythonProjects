temps = input("donner un temps en secondes ");
print(temps);
#conversion en entier
t = int(temps);
# impression numerique
print(t);
#
minutes = (t- (t % 60))/60;
restesecondes = t % 60;
#
heures = (minutes - minutes % 60)/60;
resteminutes = minutes % 60;
#1459
tf = str(int(heures)) +'h ' + str(int(resteminutes)) + 'mn ' + str(int(restesecondes)) + 's';

tf = str(int(heures)) +'h ' + str(int(resteminutes)) + 'mn ' + str(int(restesecondes)) + 's';
print(tf);

a = 'otot';
b = 'titi'
k= 2;
g = a + ' # ' + b + ' ' + (k ) ;
print(g);
