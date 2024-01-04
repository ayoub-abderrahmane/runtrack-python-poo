class Ville:
    def __init__(self ,nom ,nb_habitant):
        self.__nom = nom
        self.__nb_habitant = nb_habitant
    
    def get_nom(self):
        return self.__nom
    
    def get_nb_habitant(self):
        return self.__nb_habitant
    
    def set_ajout_nb(self ,nb_habitant):
        self.__nb_habitant = nb_habitant
        

class Personne:
    def __init__(self ,nom ,age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def ajouterPopulation(self ,ville):
        ajout = ville.get_nb_habitant() + 1
        ville.set_ajout_nb(ajout)


paris = Ville('Paris' ,1000000)
print ("Population de la ville de Paris :" ,paris.get_nb_habitant())
marseille = Ville('Marseille' ,861635)
print ("Population de la ville de Marseille :" ,marseille.get_nb_habitant())
john = Personne('John' ,45, paris)
myrtille = Personne('Myrtille' ,4, paris)
chloe = Personne('Chloe' ,18,marseille)
john.ajouterPopulation(paris)
myrtille.ajouterPopulation(paris)
chloe.ajouterPopulation(marseille)
print("Mise a jour de la population de la ville de Paris :" ,paris.get_nb_habitant())
print("Mise a jour de la population de la ville de Marseille :" ,marseille.get_nb_habitant())


