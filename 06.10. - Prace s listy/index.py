list = [1,56,2,6]
list.insert(1, 12) #vlozi prvek 12 do listu na indexu 1
print(list)
deleted = list.pop(1) #vymaze prvek na indexu 1 a ulozi do promenno
print(list)
print(deleted)
newList = range(1,10,2) #vytvori list cisel od 1 do 10 a bude se zvetsovat o 2
print(newList)
print(len(newList))

letters = ["a", "b", "c", "d", "e", "f", "g"]
sList = letters[2:6] #prvky z indexu 2 az 6
print(sList)
soList = letters[:5] #prvnich 5 prvku od zacatku
print(soList)
stList = letters[-3:] #posledni 3 prvky z listu
print(stList)
sfList = letters[:-3] #vsechny prvky krome poslednich trech
print(sfList)

lett = ["m", "m", "n", "o", "j", "j", "l"]
cou = lett.count("m") #vrati kolikrat je v listu m
print(cou)
lett.sort() #seradi prvky abecedne
print(lett)
lett.sort(reverse=True) #seradi prvky obracene
print(lett)
newLett = sorted(lett) #seradi prvky do noveho listu