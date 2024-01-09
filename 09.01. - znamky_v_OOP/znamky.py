
list = []


def prumer(list, prumer2=0):
    for i, y in enumerate (list):
        
        prumer2+=y[1]

    prumer2/=i+1
    return prumer2
class znamky:
    
    
    def __init__(self, jmeno, znamka, datum):
        self.jmeno = jmeno
        self.znamka = znamka
        self.datum = datum
        
    def zpais(self):
        
        list.append([self.jmeno, self.znamka, self.datum])
        
        
        
    def vypis(self):
        print("jmeno je " + str(self.jmeno)+ " znamka je " + str(self.znamka) + " datum je " + str(self.datum)   )
        
stepan = znamky("stepan", 1, 5.5)
stepan.vypis()
stepan.zpais()


david = znamky("david", 4, 5.5)
david.vypis()
david.zpais()

jakub = znamky("jakub", 2, 5.5)
jakub.vypis()
jakub.zpais()

print(prumer(list))
