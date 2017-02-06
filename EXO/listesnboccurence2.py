import time

temp = time.clock()
newlist=[]
tempList=[]
mylist=['q','s','q','s','a','b','a','b','c','q','a','d']
for x in mylist:
  if x not in tempList:
      tempList.append(x)
      newlist.append(x + ':' + str(mylist.count(x)))  
dif = time.clock() - temp        
print(newlist)
print(tempList)
print (dif)