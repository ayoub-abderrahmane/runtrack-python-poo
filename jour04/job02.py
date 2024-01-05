class Personne:
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print ("l'age de la personne est" ,self.age)
    
    def bonjour(self):
        print ("Hello")
    
    def modifierAge(self ,mod_age):
        self.age = mod_age

class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print ("j'ai",self.age ,"ans")


class Professeur(Personne):
    def __init__(self ,matiere):
        self.__matiereEnseignée = matiere
    
    def get_maniere(self):
        return self.__matiereEnseignée
    
    def enseigner(self):
        print ("Le cours va commencer")






personne = Personne()
eleve = Eleve()
professeur = Professeur("histoire")
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.afficherAge()
professeur.modifierAge(40)
professeur.afficherAge()
professeur.bonjour()
professeur.enseigner()