class Rectangle:
    # Initialisation de la longueur et la largeur
    def __init__(self ,longueur ,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # création des accesseur
    
    def get_long(self):
        return self.__longueur

    def get_larg(self):
        return self.__largeur
    
    # création des mutateurs
    
    def set_long(self,longueur):
        self.__longueur = longueur
    
    def set_larg(self,largeur):
        self.__largeur = largeur

call = Rectangle(10 ,5)
print (call.get_larg())

call.set_larg(20)
print (call.get_larg())

    

