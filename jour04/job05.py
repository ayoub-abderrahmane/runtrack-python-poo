from math import *

class Forme:
    def __init__(self):
        pass

    def aire(self):
        print (0)

class Rectangle(Forme):
    def __init__(self , largeur ,hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        resultat = self.largeur * self.hauteur
        print ("L'aire du rectangle est" ,resultat)


class Cercle(Forme):
    def __init__(self ,radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        surface = self.radius * pi * self.radius
        print ("l'aire du cercle est" ,surface)

rect = Rectangle(10 ,5)
rect.aire()
circle = Cercle(2)
circle.aire()
