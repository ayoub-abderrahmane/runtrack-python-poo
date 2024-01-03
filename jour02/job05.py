class Voiture:
    def __init__(self ,marque ,modele ,annee ,km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50
    
    def get_marque(self):
        return self.__marque
    
    def get_en_marche(self):
        return self.__en_marche
    
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_km(self):
        return self.__km
    
    def set_marque(self ,marque):
        self.__marque = marque
    
    def set_modele(self ,modele):
        self.__modele = modele
    
    def set_annee(self ,annee):
        self.__annee = annee
    
    def set_km(self ,km):
        self.__km = km
    
    def verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        self.__en_marche = True
        if self.verifier_plein() > 5:
            print ("La voiture peut démarrer")
        else:
            print("L'essence est insuffisante pour démarrer")
    
    def arreter(self):
        self.__en_marche = False
    
call = Voiture('Volswagen' ,'Polo' ,'2015' ,'1500')

call.demarrer()
call.get_en_marche()



