class Forme:
    def __init__(self):
        pass

    def aire():
        print (0)

class Rectangle(Forme):
    def __init__(self , largeur ,hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        resultat = self.largeur * self.hauteur
        print ("L'aire du rectangle est" ,resultat)

rect = Rectangle(10 ,5)
rect.aire()
