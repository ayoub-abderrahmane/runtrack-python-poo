class Rectangle:
    def __init__(self ,longueur ,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self ,longueur):
        self.__longueur = longueur
    
    def set_largeur(self ,largeur):
        self.__largeur = largeur

    
    def perimetre(self):
        result = self.__largeur + self.__longueur + self.__largeur + self.__longueur
        print ("Le perimetre du rectangle est" ,result)
    
    def surface(self):
        aire = self.__longueur * self.__largeur
        print ("La surface du rectangle est" ,aire)

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur ,hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self ,hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        volume = self.__hauteur * super().get_longueur() * super().get_largeur()
        print ("Le volume du parallelepipede est " ,volume)


rectangle = Rectangle(10 ,5)
rectangle.surface()
figure = Parallelepipede(10 ,5 ,2)
figure.volume()
