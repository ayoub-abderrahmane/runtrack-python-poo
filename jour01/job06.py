class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = None
        
    
    def vieillir(self):
        print ("l'age de l'animal est" ,self.age ,"ans")
        self.age += 1
        print ("l'age de l'animal est" ,self.age ,"ans")
    
    def nommer(self,prenom):
        print ("l'animal se nomme",prenom)
    
        
    
call = Animal()
call.vieillir()
call.nommer('Luna')